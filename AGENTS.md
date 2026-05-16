# AGENTS.md - 代理编码指南

## 项目概述

这是一个使用 **Butterfly 主题**的 **Hexo 静态博客**。这是一个个人技术博客，主要包含中文内容，涵盖算法、Spring Boot、Linux 等技术主题。

## 构建命令

```bash
npm run build    # 生成静态网站 (hexo generate)
npm run clean    # 清理生成的文件
npm run server   # 启动本地开发服务器 (hexo server)
npm run deploy   # 部署到 GitHub Pages
```

## 运行单个测试

本项目**没有自动化测试**。作为静态网站生成器，工作流程如下：
1. 修改源文件
2. 运行 `npm run server` 进行实时预览
3. 运行 `npm run build` 生成生产版本
4. 在 `public/` 目录中验证输出

## 代码风格指南

### JavaScript (source/js/)

**格式化：**
- 2 空格缩进
- 必须使用分号
- 字符串使用双引号
- 多行对象/数组末尾添加逗号

**命名约定：**
- 变量和函数使用 `camelCase`（小驼峰）
- 类使用 `PascalCase`（大驼峰），如 `class Cursor`
- 常量使用 `UPPER_CASE`
- 私有全局变量以下划线前缀，如 `_privateVar`

**代码结构：**
- 使用 IIFE 模式进行模块隔离：`(() => { ... })();`
- 默认使用 `const`，需要重新赋值时使用 `let`
- 避免使用 `var`
- 优先使用提前返回，避免嵌套条件语句

**示例：**
```javascript
const getStyle = (el, attr) => {
  try {
    return window.getComputedStyle(el)[attr];
  } catch (e) {}
  return "";
};

class Cursor {
  constructor() {
    this.pos = { curr: null, prev: null };
    this.init();
  }

  move(left, top) {
    this.cursor.style.left = `${left}px`;
  }
}

(() => {
  CURSOR = new Cursor();
})();
```

### CSS (source/css/)

**格式化：**
- 2 空格缩进
- 左大括号前加空格
- 每行一个属性
- 必须使用尾部分号

**命名：**
- 类和 ID 使用 `kebab-case`（短横线分隔）
- 鼓励使用 BEM 模式
- 谨慎使用 `!important`（主题中用于覆盖样式）

**深色模式：**
使用 `[data-theme="dark"]` 选择器定义深色模式样式：
```css
[data-theme="dark"] .card-widget {
  background: #1e1e1e;
  color: antiquewhite;
}
```

### 博客文章 (source/_posts/)

**Front Matter 必填字段：**
```yaml
---
title: 文章标题
date: 2025-04-05 20:02:11
tags: [标签 1, 标签 2]
categories: 分类名称
cover: /img/cover.jpg
---
```

**Front Matter 可选字段：**
- `swiper_index`: 用于首页轮播推荐文章
- `comments`: 启用/禁用评论 (true/false)

**文件命名：**
- 算法题格式：`LeetCode<题号>-标题【难度】.md`
- 允许使用中文文件名
- 单词间使用短横线分隔

### Pug 模板 (themes/butterfly/layout/)

- 2 空格缩进
- 无需闭合标签（Pug 语法）
- 使用 Mixin 实现可复用组件

### Stylus (themes/butterfly/source/css/)

- 使用 Stylus 预处理器（无需分号和花括号）
- 变量前缀使用 `$`
- 鼓励使用嵌套提高特异性

## 目录结构

```
E:\VScodeProjects\MyBlog/
├── source/              # 网站源文件
│   ├── _posts/          # 博客文章（Markdown）
│   ├── _data/           # 自定义数据文件
│   ├── css/             # 自定义 CSS
│   ├── js/              # 自定义 JavaScript
│   ├── img/             # 图片资源
│   └── about/           # 静态页面
├── themes/butterfly/    # 主题文件
│   ├── layout/          # Pug 模板
│   ├── source/          # 主题资源
│   └── scripts/         # Hexo 脚本
├── public/              # 生成的网站（已加入 gitignore）
├── _config.yml          # 站点配置
└── _config.butterfly.yml # 主题配置
```

## 配置说明

**站点配置：** `_config.yml`
- 网站标题、作者、URL
- 部署设置
- 插件配置

**主题配置：** `_config.butterfly.yml`
- 主题外观设置
- 导航菜单
- 社交链接
- 评论系统

## 部署

通过 `npm run deploy` 部署到 GitHub Pages：
- 仓库：`Ywj-ch/Ywj-ch.github.io`
- 分支：`main`

## Git 工作流

- 主分支用于开发
- 个人博客允许直接提交到 main 分支
- 无需 PR 审查

## 错误处理

**JavaScript：**
- DOM 操作使用 try-catch 包裹
- 失败时优雅降级
- 开发阶段允许控制台错误

**CSS：**
- 必要时使用 `!important` 覆盖主题样式
- 测试深色/浅色模式兼容性

## 依赖管理

```bash
# 添加新包
npm install <包名> --save

# 更新依赖
npm update

# 清洁安装
rm -rf node_modules/ && npm install
```

## 常用命令

```bash
# 创建新文章
hexo new post "文章标题"

# 生成并启动服务
hexo generate && hexo server

# 草稿工作流
hexo new draft "标题"     # 创建到 source/_drafts/
hexo publish draft "标题"  # 移动到 source/_posts/
```

## 代理注意事项

1. **没有测试** - 通过开发服务器进行手动测试
2. **中文内容** - 文章主要为中文
3. **Butterfly 主题** - 查看主题文档 https://butterfly.js.org/ 了解功能
4. **Stylus** - 主题使用 Stylus，不是普通 CSS
5. **Pug** - 模板使用 Pug，不是 EJS 或 Handlebars

## 现有规则

本项目**没有**以下规则文件：
- 无 `.cursor/rules/` 目录
- 无 `.cursorrules` 文件
- 无 `.github/copilot-instructions.md` 文件
