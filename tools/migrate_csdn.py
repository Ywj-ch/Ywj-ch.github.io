"""
博客图片迁移工具 - CSDN 版本

从 CSDN 文章页面获取图片并下载到本地

使用方法：python migrate_csdn.py
"""
import os
import re
import requests
import shutil
from datetime import datetime
from bs4 import BeautifulSoup

# 配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "..", "source", "_posts")
IMAGES_DIR = os.path.join(BASE_DIR, "..", "source", "images")
DATA_FILE = os.path.join(BASE_DIR, "..", "data.md")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://blog.csdn.net/"
}

def load_csdn_urls():
    """加载 data.md 中的 CSDN URL 映射"""
    mapping = {}
    if not os.path.exists(DATA_FILE):
        return mapping
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ' : ' in line:
                url, title = line.split(' : ', 1)
                mapping[title] = url.strip()
    return mapping

def find_csdn_url(filename, csdn_mapping):
    """根据文件名查找对应的 CSDN URL"""
    # 去掉 .md 后缀
    name = filename.replace('.md', '')
    
    # 直接匹配
    if name in csdn_mapping:
        return csdn_mapping[name]
    
    # 模糊匹配：去掉标点符号和空格后比较
    def normalize(s):
        return re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5]', '', s)
    
    name_normalized = normalize(name)
    for key, url in csdn_mapping.items():
        key_normalized = normalize(key)
        if name_normalized == key_normalized or name_normalized in key_normalized or key_normalized in name_normalized:
            return url
    
    return None

def fetch_csdn_images(csdn_url):
    """从 CSDN 文章页面获取所有图片 URL"""
    try:
        resp = requests.get(csdn_url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        images = []
        
        # CSDN 文章主体
        article = soup.find('article')
        if not article:
            article = soup.find(class_='article_content')
        
        if article:
            for img in article.find_all('img'):
                src = img.get('src') or img.get('data-src')
                if src and src.startswith('http'):
                    images.append(src)
        
        return images
    except Exception as e:
        print(f"获取 CSDN 页面失败：{e}")
        return []

def get_local_images(content):
    """获取 Markdown 中的外部图片 URL（用于匹配）"""
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    urls = []
    for match in re.finditer(pattern, content):
        url = match.group(2)
        if url.startswith('http'):
            urls.append(url)
    return urls

def download_image(url, save_path):
    """下载单张图片"""
    if os.path.exists(save_path):
        return True
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200 and len(resp.content) > 0:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            return True
    except Exception as e:
        print(f"下载失败：{url[:60]}...")
    return False

def get_ext(url):
    """获取图片扩展名"""
    for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
        if url.lower().endswith(ext):
            return ext
    name = url.split('/')[-1].split('?')[0]
    if '.' in name:
        return '.' + name.split('.')[-1]
    return '.png'

def match_images(local_urls, csdn_urls):
    """
    匹配本地 Markdown 中的图片 URL 和 CSDN 页面的图片 URL
    按顺序匹配
    """
    result = {}
    csdn_list = list(csdn_urls)
    
    for i, local_url in enumerate(local_urls):
        if i < len(csdn_list):
            result[local_url] = csdn_list[i]
        else:
            # 如果 CSDN 图片不够，保留原 URL（会下载失败）
            result[local_url] = local_url
    
    return result

def main():
    print("=" * 50)
    print("博客图片迁移工具 - CSDN 版本")
    print("=" * 50)
    
    # 创建图片目录
    os.makedirs(IMAGES_DIR, exist_ok=True)
    
    # 备份
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(BASE_DIR, "..", f"source/_posts_backup_{timestamp}")
    shutil.copytree(POSTS_DIR, backup_dir)
    print(f"已备份：{backup_dir}")
    
    # 加载 CSDN URL 映射
    csdn_mapping = load_csdn_urls()
    print(f"加载了 {len(csdn_mapping)} 个 CSDN 文章链接")
    
    # 处理每篇文章
    stats = {'total': 0, 'success': 0, 'failed': 0}
    
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取本地 Markdown 中的图片 URL
        local_urls = get_local_images(content)
        if not local_urls:
            continue
        
        # 获取对应的 CSDN URL
        csdn_url = find_csdn_url(filename, csdn_mapping)
        if not csdn_url:
            print(f"\n跳过：{filename[:40]}... (无 CSDN 链接)")
            continue
        
        print(f"\n处理：{filename[:40]}...")
        print(f"CSDN: {csdn_url[:60]}...")
        
        # 从 CSDN 获取图片
        csdn_images = fetch_csdn_images(csdn_url)
        if not csdn_images:
            print(f"  警告：未能从 CSDN 获取图片")
            csdn_images = local_urls  # 回退到原 URL
        
        print(f"  CSDN 图片数：{len(csdn_images)}, 本地引用数：{len(local_urls)}")
        
        # 创建文章图片目录
        post_name = filename.replace('.md', '')
        post_img_dir = os.path.join(IMAGES_DIR, post_name)
        os.makedirs(post_img_dir, exist_ok=True)
        
        # 匹配图片
        url_map = match_images(local_urls, csdn_images)
        
        # 下载并替换
        replace_map = {}
        for idx, (local_url, csdn_img_url) in enumerate(url_map.items(), 1):
            ext = get_ext(csdn_img_url)
            new_name = f"{idx}{ext}"
            save_path = os.path.join(post_img_dir, new_name)
            
            stats['total'] += 1
            
            if download_image(csdn_img_url, save_path):
                local_path = f"/source/images/{post_name}/{new_name}"
                replace_map[local_url] = local_path
                stats['success'] += 1
                print(f"  [{stats['success']}/{len(url_map)}] OK")
            else:
                stats['failed'] += 1
                print(f"  [FAIL] {idx}")
        
        # 替换链接
        for local_url, local_path in replace_map.items():
            content = content.replace(f']({local_url})', f']({local_path})')
        
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
