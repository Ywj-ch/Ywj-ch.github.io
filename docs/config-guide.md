# 配置说明（中文）

本文档用中文解释项目中的关键配置项。

---

## 目录

1. [_config.yml](#一-configyml-站点配置) - 站点配置
2. [_config.butterfly.yml](#二-configbutterflyyml-主题配置) - 主题配置

---

## 一、`_config.yml` - 站点配置

这是 Hexo 博客的主配置文件。

### 站点信息

```yaml
title: 爱吃薯片的熊猫の技术小站    # 网站标题
subtitle: "记录学习与成长"         # 副标题
description: "Dream big..."        # 网站描述
author: 爱吃薯片的熊猫              # 作者名
language:                          # 语言
  - zh-CN
  - en
```

### URL 配置

```yaml
url: https://chippanda.top/        # 网站域名
permalink: :year/:month/:day/:title/  # 文章链接格式
```

### 目录配置

```yaml
source_dir: source                 # 源文件目录
public_dir: public                 # 生成的网站目录
tag_dir: tags                      # 标签目录
archive_dir: archives              # 归档目录
category_dir: categories           # 分类目录
```

### 文章配置

```yaml
new_post_name: :title.md           # 新建文章的文件名格式
default_layout: post               # 默认文章类型
post_asset_folder: false           # 是否为每篇文章创建独立资源文件夹
relative_link: false               # 是否使用相对链接
```

### 代码高亮

```yaml
syntax_highlighter: highlight.js   # 语法高亮器
highlight:
  enable: false                    # 禁用 Hexo 默认高亮
prismjs:
  preprocess: true                 # 启用 PrismJS 预处理
  line_number: true                # 显示行号
```

### 首页配置

```yaml
index_generator:
  path: ""                         # 首页路径
  per_page: 10                     # 每页显示 10 篇文章
  order_by: -date                  # 按日期倒序排列
```

### 分页配置

```yaml
per_page: 6                        # 每页显示 6 篇文章
pagination_dir: page               # 分页目录名
```

### 日期格式

```yaml
date_format: YYYY-MM-DD            # 日期格式
time_format: HH:mm:ss              # 时间格式
updated_option: "mtime"            # 更新时间选项
```

### 主题配置

```yaml
theme: butterfly                   # 使用 Butterfly 主题
```

### 部署配置

```yaml
deploy:
  type: git                        # 部署方式
  repo: git@github.com:...         # GitHub 仓库地址
  branch: main                     # 部署分支
```

### 图片懒加载

```yaml
lazyload:
  enable: true                     # 启用图片懒加载
  loadingImg: /img/loading.gif     # 加载中的图片
```

### Live2D 看板娘

```yaml
live2d:
  enable: false                    # 是否启用（默认关闭）
  model:
    use: live2d-widget-model-koharu # 模型（小喵）
  display:
    position: left                 # 位置
    width: 150                     # 宽度
    height: 300                    # 高度
  mobile:
    show: false                    # 手机端不显示
```

### 信封评论区

```yaml
envelope_comment:
  enable: true                     # 启用信封评论区
  custom_pic:
    cover: ...                     # 信笺头部图片
    line: ...                      # 信笺底部图片
  message:                         # 信笺正文
    - 有什么想问的？
    - 有什么想说的？
    - ...
  bottom: 自动书记人偶竭诚为您服务！  # 底部文字
```

### 分类磁贴

```yaml
magnet:
  enable: true                     # 启用分类磁贴
  type: categories                 # 按分类显示
  display:
    - name: 学习笔记
      display_name: 爱吃薯片的熊猫の学习笔记
      icon: 📚
    - name: 生活趣闻
      display_name: 爱吃薯片的熊猫の生活趣闻
      icon: 🐱‍👓
    - ...
  color_setting:
    text_color: black              # 文字颜色
    background_color: "#f2f2f2"    # 背景颜色
    background_hover_color: "#69e8f2" # 悬停背景颜色
```

### 首页轮播图

```yaml
swiper:
  enable: true                     # 启用轮播图
  timemode: date                   # 按创建时间排序
  default_descr: 再怎么看我也不知道... # 默认描述
```

### 动画效果

```yaml
wowjs:
  enable: true                     # 启用动画
  mobile: false                    # 移动端禁用
  animateitem:
    - class: recent-post-item      # 文章卡片动画
      style: animate__fadeInDown
      duration: 2s
    - class: card-widget            # 小部件动画
      style: animate__zoomIn
```

### 文章加密

```yaml
encrypt:
  abstract: 有东西被加密了，请输入密码查看.
  message: 您好，这里需要密码.
  tags:
    - { name: tagName, password: 密码 A }
  theme: xray                      # 加密主题
```

---

## 二、`_config.butterfly.yml` - 主题配置

这是 Butterfly 主题的配置文件。

### 导航栏

```yaml
nav:
  logo:                            # 导航栏 logo（空则不显示）
  display_title: true              # 显示标题
  fixed: false                     # 导航栏是否固定

menu:
  首页：/ || fas fa-home
  归档：/archives/ || fas fa-archive
  标签：/tags/ || fas fa-tags
  分类：/categories/ || fas fa-folder-open
  列表 || fa fa-list || hide:       # 有子菜单
    音乐：/music/ || fas fa-music
    照片：/picture/ || fas fa-images
    电影：/movies/ || fas fa-video
  留言板：/comments/ || fas fa-envelope-open
  友链：/link/ || fas fa-link
  关于：/about/ || fas fa-heart
```

### 代码块

```yaml
code_blocks:
  theme: light                     # 代码主题：darker/pale night/light/ocean/mac
  macStyle: false                  # Mac 风格窗口
  height_limit: false              # 代码块高度限制
  copy: true                       # 显示复制按钮
  language: true                   # 显示语言标签
  shrink: true                     # 代码块默认折叠
```

### 自定义代码配置

```yaml
highlight_theme: mac               # 代码主题
highlight_copy: true               # 复制按钮
highlight_lang: false              # 显示语言
highlight_shrink: true             # 默认折叠
highlight_height_limit: false      # 高度限制
code_word_wrap: true               # 自动换行
```

### 社交链接

```yaml
social:
  fas fa-book: https://blog.csdn.net/... || CSDN || '#d81e06'
  fas fa-code-branch: https://gitee.com/... || Gitee || '#C71D23'
```

### 灯笼装饰

```yaml
lantern:
  enable: false                    # 建议只在过年期间开启
```

### 网站图标和头像

```yaml
favicon: /img/favicon.png          # 网站图标

avatar:
  img: /img/butterfly-icon.png     # 头像
  effect: false                    # 头像动画
```

### 背景图片

```yaml
disable_top_img: false             # 是否禁用顶部背景图
default_top_img: rgba(0, 0, 0, 0)  # 默认顶部背景图
index_img:                         # 首页背景图
background: /img/【哲风壁纸】海边...png # 网站背景
```

### 封面图片

```yaml
cover:
  index_enable: true               # 首页显示封面
  aside_enable: true               # 侧边栏显示封面
  archives_enable: true            # 归档页显示封面
  default_cover:
    - "/img/default-cover.jpg"     # 默认封面
```

### 404 页面

```yaml
error_img:
  flink: /img/friend_404.gif       # 友链 404 图片
  post_page: /img/404.jpg          # 文章页 404 图片

error_404:
  enable: true                     # 启用 404 页面
  subtitle: "Page Not Found"
  background: /img/error-page.png
```

### 文章信息

```yaml
post_meta:
  page:                            # 首页
    date_type: created             # 显示创建日期
    date_format: date              # 日期格式
    categories: true               # 显示分类
    tags: false                    # 不显示标签
  post:                            # 文章页
    position: left                 # 位置
    date_type: both                # 显示创建和更新日期
```

### 首页设置

```yaml
index_site_info_top:               # 首页信息位置
index_top_img_height:              # 首页顶部图片高度

subtitle:
  enable: true                     # 启用副标题
  effect: true                     # 打字机效果
  loop: true                       # 循环播放
  sub:
    - Dare to dream Live to shine! 🌟💫
    - Time flows gently Cherish each moment! ⏳🍃

index_layout: 3                    # 文章布局：1-7 种样式
index_post_content:
  method: 3                        # 显示文章摘要：1=description, 2=both, 3=auto_excerpt
  length: 500                      # 摘要长度
```

### 文章目录

```yaml
toc:
  post: true                       # 文章显示目录
  page: false                      # 页面不显示目录
  number: true                     # 显示序号
  expand: false                    # 不自动展开
  style_simple: false              # 简洁模式
  scroll_percent: true             # 显示阅读进度
```

### 版权声明

```yaml
post_copyright:
  enable: true                     # 启用版权声明
  decode: false                    # 不加密
  license: CC BY-NC-SA 4.0         # 许可协议
  license_url: https://...         # 许可协议链接
```

### 打赏

```yaml
reward:
  enable: false                    # 禁用打赏
```

### 相关文章

```yaml
related_post:
  enable: true                     # 启用相关文章
  limit: 6                         # 显示 6 篇
  date_type: created               # 按创建时间排序
```

### 文章导航

```yaml
post_pagination: 1                 # 启用文章分页导航
```

### 页脚

```yaml
footer:
  owner:
    enable: true                   # 显示站长信息
    since: 2024                    # 博客成立年份
  copyright: flase                 # 显示 Copyright
```

### 侧边栏

```yaml
aside:
  enable: true                     # 启用侧边栏
  hide: false                      # 不隐藏
  button: true                     # 显示隐藏按钮
  mobile: true                     # 移动端显示
  position: right                  # 位置

  card_author:                     # 作者卡片
    enable: true
    button:
      enable: true
      icon: fab fa-github
      text: Follow Me
      link: https://github.com/Ywj-ch

  card_announcement:               # 公告卡片
    enable: true
    content: 欢迎来到我的博客！

  card_recent_post:                # 最新文章
    enable: true
    limit: 5                       # 显示 5 篇

  card_post_series:                # 文章系列
    enable: true
```

---

## 常用配置速查

| 配置项 | 文件 | 推荐值 |
|--------|------|--------|
| 网站标题 | `_config.yml` | 你的博客名 |
| 作者名 | `_config.yml` | 你的名字 |
| 域名 | `_config.yml` | `https://你的域名/` |
| 部署仓库 | `_config.yml` | `git@github.com:用户名/用户名.github.io.git` |
| 导航菜单 | `_config.butterfly.yml` | 按需配置 |
| 社交链接 | `_config.butterfly.yml` | 你的社交账号 |
| 代码主题 | `_config.butterfly.yml` | `mac` 或 `light` |
| 侧边栏位置 | `_config.butterfly.yml` | `right` 或 `left` |

---

**最后更新**：2026-03-01
