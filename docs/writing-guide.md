# 写作规范

本文档介绍博客文章的写作规范和格式要求。

---

## 文章位置

所有文章放在 `source/_posts/` 目录下。

---

## 文件命名

### 算法题

```
LeetCode<题号>-标题【难度】.md
```

**示例**：
- `LeetCode1863-找出所有子集的异或和再求和【简单】.md`
- `LeetCode368-最大整除子集【中等】.md`
- `LeetCode416-分割等和子集【中等】.md`

### 技术教程

```
<主题>-<内容>.md
```

**示例**：
- `Linux（Centos7）安装 docker、mysql 踩坑总结.md`
- `Spring-Boot-Vue-前后端分离项目上线实记.md`

---

## Front Matter

每篇文章开头需要包含 Front Matter（用 `---` 包裹）：

```yaml
---
title: 文章标题
date: 2025-04-05 20:02:11
tags: [标签 1, 标签 2]
categories: 分类名称
cover: /img/cover.jpg
---
```

### 必填字段

| 字段 | 说明 | 示例 |
|------|------|------|
| `title` | 文章标题 | `LeetCode1863-找出所有子集的异或和再求和【简单】` |
| `date` | 创建时间 | `2025-04-05 20:02:11` |
| `tags` | 标签（数组） | `[位运算，数组，回溯]` |
| `categories` | 分类 | `算法学习` |

### 可选字段

| 字段 | 说明 | 示例 |
|------|------|------|
| `cover` | 封面图片 | `/img/leetcode.jpg` |
| `swiper_index` | 轮播图索引（数字越小越靠前） | `7` |
| `comments` | 是否启用评论 | `true` |

---

## 文章结构

推荐的文章结构：

```markdown
---
title: 文章标题
date: 2025-04-05 20:02:11
tags: [标签 1, 标签 2]
categories: 分类名称
---

## 相关标签

> 标签 1、标签 2

## 题目简介

> 题目描述...

## 示例

> 示例 1：
> ...

## 解题思路

> 思路描述...

## 代码实现

```java
// 代码内容
```

## 总结

总结内容...
```

---

## 图片使用

### 图片存放

图片放在 `source/images/年份/文章名/` 目录下：

```
source/images/
└── 2025/
    └── linux-docker-mysql/
        ├── 1.png
        ├── 2.png
        └── 3.png
```

### 图片引用

```markdown
![描述文字](/images/2025/linux-docker-mysql/1.png)
```

### 图片命名

按文章中出现的顺序编号：`1.png`, `2.png`, `3.png`...

---

## 代码块

使用三个反引号包裹代码，并指定语言：

````markdown
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
````

支持的语言：`java`, `python`, `javascript`, `cpp`, `sql`, `yaml`, `bash` 等。

---

## 分类和标签

### 推荐分类

| 分类 | 说明 |
|------|------|
| 算法学习 | LeetCode 题解、算法笔记 |
| 学习笔记 | 技术教程、学习笔记 |
| 个人项目 | 个人项目实战 |
| 生活趣闻 | 生活相关 |

### 推荐标签

根据文章内容自定义，常用标签：
- 算法类：`位运算`, `动态规划`, `回溯`, `二分`, `数组`
- 技术类：`SpringBoot`, `Vue`, `Linux`, `Docker`, `微服务`

---

## 创建新文章

### 方式一：使用 hexo 命令

```bash
hexo new post "文章标题"
```

会在 `source/_posts/` 创建文章模板。

### 方式二：手动创建

在 `source/_posts/` 目录下创建 `.md` 文件，添加 Front Matter 后开始写作。

---

## 预览文章

```bash
# 启动本地服务器
hexo server

# 访问 http://localhost:4000/ 预览
```

---

## 检查清单

发布前检查：
- [ ] Front Matter 完整（title, date, tags, categories）
- [ ] 图片已下载到本地
- [ ] 图片路径正确
- [ ] 代码块语法高亮正常
- [ ] 分类和标签正确
- [ ] 本地预览正常

---

**最后更新**：2026-03-01
