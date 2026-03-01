# 博客工具脚本

## 目录结构

```
tools/
├── README.md                    # 本文件
├── image-migration/             # 图片迁移工具
│   ├── README.md               # 使用说明
│   ├── main.py                 # 主程序（废弃）
│   ├── migrate_csdn.py         # CSDN 图片下载（推荐使用）⭐
│   ├── migrate_simple.py       # 简化版迁移工具
│   ├── scanner.py              # 扫描模块
│   ├── downloader.py           # 下载模块
│   ├── replacer.py             # 替换模块
│   └── config.py               # 配置文件
└── docs/                        # 文档
    ├── 项目优化计划书.md        # 完整优化计划
    └── 优化计划简版.md          # 简化版计划
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

### 各模块说明

| 文件 | 作用 | 状态 |
|------|------|------|
| `migrate_csdn.py` | 从 CSDN 下载图片并替换链接 | ✅ 推荐使用 |
| `migrate_simple.py` | 简化版迁移工具 | ⚠️ 备用方案 |
| `scanner.py` | 扫描 Markdown 中的图片链接 | 🔧 模块 |
| `downloader.py` | 下载图片到本地 | 🔧 模块 |
| `replacer.py` | 替换 Markdown 中的链接 | 🔧 模块 |
| `config.py` | 配置路径和参数 | 🔧 模块 |

## 注意事项

1. **不要删除 `tools/` 目录** - 包含迁移工具，后续可能用到
2. **Python 版本** - 需要 Python 3.6+
3. **依赖安装** - 首次使用需安装 `requests` 和 `beautifulsoup4`

## 相关文档

- [项目优化计划书](./docs/项目优化计划书.md) - 完整的优化方案
- [优化计划简版](./docs/优化计划简版.md) - 快速参考

## 历史

- 2026-03-01：完成图片迁移（161 张图片，6 篇文章）
- 2026-03-01：重构工具目录结构
