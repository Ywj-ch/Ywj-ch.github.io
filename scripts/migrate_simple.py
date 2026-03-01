"""
博客图片迁移工具 - 简化版

使用方法：python migrate_simple.py
"""
import os
import re
import requests
import shutil
from datetime import datetime

# 配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "..", "source", "_posts")
IMAGES_DIR = os.path.join(BASE_DIR, "..", "source", "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

IMAGE_PATTERN = r'!\[([^\]]*)\]\(([^)]+)\)'

def scan_images(content):
    """提取 Markdown 内容中的外部图片链接"""
    images = []
    for match in re.finditer(IMAGE_PATTERN, content):
        url = match.group(2)
        if url.startswith('http'):
            images.append({
                'alt': match.group(1),
                'url': url,
                'match': match.group(0)
            })
    return images

def download_image(url, save_path):
    """下载单张图片"""
    if os.path.exists(save_path):
        return True
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            return True
    except Exception as e:
        print(f"下载失败：{url[:60]} - {e}")
    return False

def get_ext(url):
    """获取图片扩展名"""
    for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
        if url.lower().endswith(ext):
            return ext
    # 从 URL 中提取
    name = url.split('/')[-1].split('?')[0]
    if '.' in name:
        return '.' + name.split('.')[-1]
    return '.png'

def main():
    print("=" * 50)
    print("博客图片迁移工具")
    print("=" * 50)
    
    # 创建图片目录
    os.makedirs(IMAGES_DIR, exist_ok=True)
    
    # 备份
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(BASE_DIR, "..", f"source/_posts_backup_{timestamp}")
    shutil.copytree(POSTS_DIR, backup_dir)
    print(f"已备份：{backup_dir}")
    
    # 处理每篇文章
    stats = {'total': 0, 'success': 0, 'failed': 0}
    
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        images = scan_images(content)
        if not images:
            continue
        
        print(f"\n处理：{filename[:40]}... ({len(images)}张图)")
        
        # 创建文章图片目录
        post_name = filename.replace('.md', '')
        post_img_dir = os.path.join(IMAGES_DIR, post_name)
        os.makedirs(post_img_dir, exist_ok=True)
        
        # 去重
        seen = set()
        unique_images = []
        for img in images:
            if img['url'] not in seen:
                seen.add(img['url'])
                unique_images.append(img)
        
        # 下载并替换
        url_map = {}
        for idx, img in enumerate(unique_images, 1):
            url = img['url']
            ext = get_ext(url)
            new_name = f"{idx}{ext}"
            save_path = os.path.join(post_img_dir, new_name)
            
            stats['total'] += 1
            
            if download_image(url, save_path):
                local_path = f"/source/images/{post_name}/{new_name}"
                url_map[url] = local_path
                stats['success'] += 1
                print(f"  [{stats['success']}/{len(unique_images)}] OK")
            else:
                stats['failed'] += 1
        
        # 替换链接
        for url, local in url_map.items():
            content = content.replace(f']({url})', f']({local})')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print("\n" + "=" * 50)
    print("完成!")
    print(f"成功：{stats['success']}/{stats['total']}")
    if stats['failed'] > 0:
        print(f"失败：{stats['failed']}")
    print("=" * 50)

if __name__ == "__main__":
    main()
