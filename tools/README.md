# 博客图片迁移脚本

## 功能说明

该脚本用于将博客文章中的外部图片链接（CSDN 等）批量下载到本地，并自动替换 Markdown 文件中的链接为本地路径。

## 目录结构

```
scripts/
├── main.py          # 主程序入口
├── config.py        # 配置文件
├── scanner.py       # 扫描模块
├── downloader.py    # 下载模块
├── replacer.py      # 替换模块
└── README.md        # 说明文档
```

## 使用方法

### 1. 安装依赖

```bash
pip install requests
```

### 2. 配置 data.md

在项目根目录创建 `data.md` 文件，格式如下：

```
https://blog.csdn.net/xxx/article/details/123 : 文章标题
```

### 3. 运行脚本

```bash
cd scripts
python main.py
```

## 执行流程

1. **扫描**：遍历 `source/_posts/` 所有 Markdown 文件，提取外部图片链接
2. **备份**：自动备份文章目录到 `source/_posts_backup_时间戳/`
3. **下载**：从 CSDN 下载图片到 `source/images/文章名/序号.png`
4. **替换**：替换 Markdown 中的图片链接为本地路径

## 输出示例

```
source/images/
├── LeetCode1863-找出所有子集的异或和再求和【简单】/
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
├── Linux（Centos7）安装 docker、mysql 踩坑总结/
│   ├── 1.png
│   ├── 2.png
│   └── ...
└── ...
```

## 配置选项

在 `config.py` 中可修改：

| 选项 | 说明 | 默认值 |
|------|------|--------|
| POSTS_DIR | 文章目录 | source/_posts |
| IMAGES_DIR | 图片目录 | source/images |
| DATA_FILE | 映射文件 | data.md |
| TIMEOUT | 下载超时 | 30 秒 |
| MAX_RETRIES | 最大重试 | 3 次 |

## 故障排除

### 图片下载失败
- 检查网络连接
- CSDN 可能有反爬，脚本已添加请求头模拟浏览器
- 查看控制台错误信息

### 替换后图片不显示
- 检查路径是否正确（以 `/source/images/` 开头）
- 运行 `npm run server` 预览
- 清除浏览器缓存

## 回滚方法

如果迁移后出现问题，可以从备份恢复：

```bash
# 删除已修改的文章
rm -rf source/_posts/*

# 恢复备份
cp -r source/_posts_backup_时间戳/* source/_posts/

# 删除备份（可选）
rm -rf source/_posts_backup_时间戳
```
