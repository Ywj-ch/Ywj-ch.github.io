# 爱吃薯片的熊猫の技术小站

个人技术博客，使用 Hexo + Butterfly 主题搭建。

🔗 **在线访问**：https://chippanda.top/

---

## 快速开始

### 安装依赖

```bash
npm install
```

### 本地预览

```bash
# 方式 1：使用 npm scripts（推荐）
npm run server

# 方式 2：直接使用 hexo 命令
hexo server
```

访问 http://localhost:4000/ 预览博客。

### 生成静态文件

```bash
npm run build
# 或
hexo generate
```

生成的网站在 `public/` 目录。

### 部署到 GitHub Pages

```bash
npm run deploy
# 或
hexo deploy
```

---

## 目录结构

```
MyBlog/
├── source/              # 网站源文件
│   ├── _posts/          # 博客文章（Markdown）
│   ├── images/          # 图片资源（按年份分类）
│   │   ├── 2024/
│   │   ├── 2025/
│   │   └── common/
│   ├── css/             # 自定义 CSS
│   ├── js/              # 自定义 JavaScript
│   └── about/           # 静态页面
├── docs/                # 项目文档
├── tools/               # 工具脚本
│   └── image-migration/ # 图片迁移工具
├── themes/butterfly/    # 主题文件
├── public/              # 生成的网站（gitignore）
├── _config.yml          # 站点配置
├── _config.butterfly.yml # 主题配置
└── package.json         # 项目依赖
```

---

## 常用命令

| 命令 | 作用 |
|------|------|
| `hexo server` | 启动本地服务器 |
| `hexo clean` | 清理缓存 |
| `hexo generate` | 生成静态网站 |
| `hexo deploy` | 部署到 GitHub |
| `hexo new post "标题"` | 创建新文章 |
| `hexo new page "页面名"` | 创建新页面 |
| `npm run build` | 生成静态网站 |
| `npm run server` | 启动本地服务器 |
| `npm run deploy` | 部署到 GitHub |

---

## 文档导航

| 文档 | 说明 |
|------|------|
| [部署流程](./deploy.md) | 如何部署到 GitHub Pages |
| [写作规范](./writing-guide.md) | 博客文章格式规范 |
| [图片使用规范](./image-guide.md) | 图片存放和引用规范 |
| [配置说明](./config-guide.md) | 配置文件中文说明 |

---

## 技术栈

- **框架**：Hexo 7.3.0
- **主题**：Butterfly
- **部署**：GitHub Pages
- **域名**：chippanda.top

---

## 开发规范

### 文章命名
- 算法题：`LeetCode<题号>-标题【难度】.md`
- 技术教程：简洁明了的中文标题

### 图片存放
- 按年份分类：`source/images/年份/文章名/`
- 图片命名：`1.png`, `2.png`, `3.png`...（按出现顺序）

### Git 提交
- 定期提交到 main 分支
- 提交信息清晰描述变更内容

---

**最后更新**：2026-03-01
