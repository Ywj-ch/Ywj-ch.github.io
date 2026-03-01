"""
博客图片迁移工具 - 配置文件
"""
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 文章目录
POSTS_DIR = os.path.join(BASE_DIR, "source", "_posts")

# 图片存储目录
IMAGES_DIR = os.path.join(BASE_DIR, "source", "images")

# CSDN 文章映射文件
DATA_FILE = os.path.join(BASE_DIR, "data.md")

# 请求头（模拟浏览器）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://blog.csdn.net/"
}

# 下载超时时间（秒）
TIMEOUT = 15

# 最大重试次数
MAX_RETRIES = 3

# 图片链接匹配正则
IMAGE_PATTERN = r'!\[([^\]]*)\]\(([^)]+)\)'
