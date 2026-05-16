# 图片使用规范

本文档介绍博客图片的存放和引用规范。

---

## 目录结构

图片统一存放在 `source/images/` 目录下，按年份分类：

```
source/images/
├── 2024/                    # 2024 年的文章图片
│   ├── hexo-blog-setup/     # 文章 1
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   └── python-fiddler-library/
│       └── ...
├── 2025/                    # 2025 年的文章图片
│   ├── linux-docker-mysql/
│   ├── springboot-vue-project/
│   ├── springboot-ruoyi/
│   ├── microservice-springcloud/
│   └── ...
└── common/                  # 公共资源
    ├── default-cover.jpg
    └── 404.jpg
```

---

## 目录命名

目录名使用文章标题的拼音或英文简写：

| 文章标题 | 目录名 |
|----------|--------|
| Linux（Centos7）安装 docker、mysql 踩坑总结 | `linux-docker-mysql` |
| Spring-Boot-Vue-前后端分离项目上线实记 | `springboot-vue-project` |
| 基于若依框架的 SpringBoot 管理系统学习 | `springboot-ruoyi` |
| 微服务入门：服务调用流程解析 | `microservice-springcloud` |
| 用 Python 与 Fiddler 实现图书馆座位自动预约 | `python-fiddler-library` |
| 基于 Hexo 框架和 Butterfly 主题搭建个人博客网站 | `hexo-blog-setup` |

---

## 图片命名

图片按在文章中出现的顺序编号：

```
1.png, 2.png, 3.png, ...
```

**不要使用**原来的文件名（如 `pic_xxxxxx.png`）。

---

## 引用方式

在 Markdown 中引用图片：

```markdown
![描述文字](/images/2025/linux-docker-mysql/1.png)
```

### 路径格式

- ✅ 正确：`/images/年份/目录名/序号.png`
- ❌ 错误：`/source/images/...`（不要包含 source）
- ❌ 错误：`./images/...`（不要用相对路径）

---

## 图片迁移

如果需要从外部链接（如 CSDN）迁移图片，使用工具脚本：

```bash
cd tools/image-migration
python migrate_csdn.py
```

工具会自动：
1. 扫描文章中的外部图片链接
2. 从 CSDN 下载图片到本地
3. 替换文章中的图片链接

---

## 公共资源

`common/` 目录存放公共图片：

| 文件 | 用途 |
|------|------|
| `default-cover.jpg` | 默认封面 |
| `404.jpg` | 404 页面图片 |
| `avatar.png` | 头像 |
| `favicon.png` | 网站图标 |

---

## 图片格式

推荐使用格式：

| 类型 | 格式 | 说明 |
|------|------|------|
| 截图 | PNG | 无损压缩，清晰度高 |
| 照片 | JPG | 有损压缩，文件小 |
| 图标 | PNG/SVG | 支持透明背景 |
| 动图 | GIF | 简单动画 |

---

## 图片大小

建议控制图片大小：

| 类型 | 建议大小 |
|------|----------|
| 文章截图 | < 500KB |
| 封面图片 | < 1MB |
| 头像/图标 | < 50KB |

过大的图片会影响加载速度。

---

## 检查清单

添加图片前检查：
- [ ] 图片已下载到本地
- [ ] 目录名正确（英文、简短）
- [ ] 图片按顺序编号（1.png, 2.png...）
- [ ] 引用路径正确（`/images/年份/目录名/序号.png`）
- [ ] 图片大小合理（< 500KB）

---

## 常见问题

### Q1: 图片不显示？
- 检查路径是否正确（应该是 `/images/...` 不是 `/source/images/...`）
- 检查图片是否在正确的目录下
- 运行 `hexo clean && hexo generate` 重新生成

### Q2: 如何批量迁移图片？
使用 `tools/image-migration/migrate_csdn.py` 脚本。

### Q3: 图片太大怎么办？
使用在线压缩工具（如 TinyPNG）压缩后再上传。

---

**最后更新**：2026-03-01
