# 图片迁移工具使用说明

## 功能说明

该工具用于批量从 CSDN 下载图片到本地，并自动替换 Markdown 文件中的图片链接。

## 依赖安装

```bash
pip install requests beautifulsoup4
```

## 使用方法

### 1. 准备 data.md 文件

在项目根目录创建 `data.md`，格式如下：

```
https://blog.csdn.net/xxx/article/details/123 : 文章标题
```

### 2. 运行脚本

```bash
cd tools/image-migration
python migrate_csdn.py
```

### 3. 执行流程

1. **扫描**：遍历 `source/_posts/` 所有 Markdown 文件
2. **备份**：自动备份文章目录
3. **下载**：从 CSDN 下载图片到 `source/images/年份/文章名/序号.png`
4. **替换**：替换 Markdown 中的图片链接为本地路径

## 输出示例

```
source/images/
├── 2025/
│   ├── leetcode-1863/
│   └── linux-docker-mysql/
└── 2024/
    └── hexo-blog-setup/
```

## 故障排除

### 图片下载失败
- 检查网络连接
- CSDN 可能有反爬，脚本已添加请求头模拟浏览器
- 查看控制台错误信息

### 替换后图片不显示
- 检查路径是否正确（以 `/images/` 开头）
- 运行 `hexo server` 预览
- 清除浏览器缓存

## 成功案例

本次项目迁移成果：
- ✅ 下载图片：161 张
- ✅ 处理文章：6 篇

---

**最后更新**：2026-03-01
