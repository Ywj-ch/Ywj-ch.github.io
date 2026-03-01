# 博客工具脚本

## 目录结构

```
tools/
├── README.md                    # 本文件
└── image-migration/             # 图片迁移工具
    ├── README.md               # 使用说明
    └── migrate_csdn.py         # CSDN 图片下载（主程序）⭐
```

## 快速开始

### 图片迁移（从 CSDN 下载图片）

```bash
# 1. 安装依赖
pip install requests beautifulsoup4

# 2. 准备 data.md 文件（项目根目录）
# 格式：CSDN 文章 URL : 文章标题

# 3. 运行迁移脚本
cd tools/image-migration
python migrate_csdn.py
```

## 工具说明

| 文件 | 作用 |
|------|------|
| `migrate_csdn.py` | 从 CSDN 下载图片并替换链接 |

## 注意事项

1. **不要删除 `tools/` 目录** - 包含迁移工具，后续可能用到
2. **Python 版本** - 需要 Python 3.6+
3. **依赖安装** - 首次使用需安装 `requests` 和 `beautifulsoup4`

## 历史

- 2026-03-01：完成图片迁移（161 张图片，6 篇文章）
- 2026-03-01：重构工具目录结构
- 2026-03-01：清理废弃脚本和文档
