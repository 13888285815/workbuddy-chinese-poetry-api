# WorkBuddy 古诗词殿堂 Web UI

一个美观的古诗词浏览和管理界面，基于中国古诗词 API 服务。

## 🌟 功能特点

- 📜 **古诗词浏览** - 浏览唐诗、宋词、元曲等经典诗词
- 🔍 **智能搜索** - 按标题、作者、内容快速搜索
- 📅 **朝代筛选** - 按朝代（唐、宋、元、明、清）筛选
- 📝 **类型分类** - 按类型（诗、词、曲）分类浏览
- ❤️ **收藏功能** - 收藏喜欢的诗词，支持本地存储
- 📋 **一键复制** - 快速复制诗词内容
- 🎲 **随机推荐** - 随机推荐一首诗词，发现更多精彩
- 🎨 **美观界面** - 现代化设计，流畅的交互动画

## 🚀 快速开始

### 本地运行

```bash
# 方法1: 使用 Python
cd web
python3 -m http.server 8080

# 方法2: 使用 Node.js
npx serve .

# 方法3: 直接打开
# 双击 index.html 文件
```

访问 `http://localhost:8080` 即可使用。

### 在线访问

GitHub Pages 在线演示：https://13888285815.github.io/workbuddy-chinese-poetry-api/web/

## 📖 使用指南

### 搜索诗词
1. 在顶部搜索框中输入关键词
2. 可选择朝代和类型进行筛选
3. 点击「搜索」按钮查看结果

### 浏览详情
1. 点击诗词卡片查看详细信息
2. 可以收藏、复制或返回列表

### 分类浏览
使用顶部导航栏的标签：
- 全部：查看所有诗词
- 诗：查看古体诗和近体诗
- 词：查看宋词等
- 曲：查看元曲等
- 收藏：查看已收藏的诗词

### 随机发现
点击「随机一首」按钮，系统会随机推荐一首诗词。

## 🛠️ 技术栈

- **前端**: HTML5 + CSS3 + JavaScript (原生)
- **UI设计**: 现代化渐变背景，卡片式布局
- **数据**: 中国古诗词 API / 本地示例数据
- **存储**: LocalStorage (收藏功能)

## 📁 项目结构

```
web/
├── index.html          # 主页面
└── .nojekyll           # GitHub Pages 配置
```

## 🔗 相关链接

- 🌐 在线演示: https://13888285815.github.io/workbuddy-chinese-poetry-api/web/
- 📦 后端API: https://github.com/13888285815/workbuddy-chinese-poetry-api
- 📚 数据来源: https://github.com/chinese-poetry/chinese-poetry

## 📄 License

MIT License
