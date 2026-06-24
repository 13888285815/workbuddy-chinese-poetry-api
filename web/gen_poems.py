#!/usr/bin/env python3
"""
意念古诗文大全 - 数据生成工具

用法:
  python3 gen_poems.py                    # 从 poems.json 生成 poems.js
  python3 gen_poems.py --edit             # 编辑 poems.json（将启动系统编辑器）
  python3 gen_poems.py --validate         # 仅验证数据完整性

说明:
  在 poems.json 中编辑诗文数据后，运行此脚本生成 poems.js。
  poems.js 被 index.html 以 <script src="poems.js"> 加载，
  在 file:// 协议下作为 fetch() 的回退数据源。
"""

import json, sys, os, subprocess, tempfile

POEMS_JSON = os.path.join(os.path.dirname(__file__), "poems.json")
POEMS_JS = os.path.join(os.path.dirname(__file__), "poems.js")

def load_json():
    with open(POEMS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def save_js(poems):
    content = f"// 自动生成 - 请勿手动编辑\n// 修改 poems.json 后运行 python3 gen_poems.py 重新生成\nconst POEMS_DATA = {json.dumps(poems, ensure_ascii=False, indent=2)};\n"
    with open(POEMS_JS, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 已生成 {POEMS_JS} ({len(poems)} 首诗文)")

def validate():
    poems = load_json()
    errors = []
    seen_ids = set()
    for p in poems:
        if "id" not in p:
            errors.append(f"缺少 id: {p.get('title', '?')}")
        elif p["id"] in seen_ids:
            errors.append(f"重复 id: {p['id']}")
        seen_ids.add(p.get("id"))
        for field in ["title", "author", "dynasty", "type", "content"]:
            if field not in p or not p[field]:
                errors.append(f"id={p.get('id', '?')} 缺少字段 '{field}'")
    if errors:
        print(f"❌ 数据验证发现 {len(errors)} 个问题:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"✅ 数据验证通过 ({len(poems)} 首诗文)")
    return poems

def edit_poems():
    validate()
    editor = os.environ.get("EDITOR") or os.environ.get("VISUAL") or "vim"
    subprocess.call([editor, POEMS_JSON])

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "--edit":
            edit_poems()
            save_js(load_json())
        elif cmd == "--validate":
            validate()
        else:
            print(f"未知参数: {cmd}")
            sys.exit(1)
    else:
        validate()
        save_js(load_json())

if __name__ == "__main__":
    main()
