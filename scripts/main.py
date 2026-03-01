"""
博客图片迁移工具 - 主程序

功能：
1. 扫描所有 Markdown 文章中的外部图片链接
2. 从 CSDN 下载图片到本地
3. 替换 Markdown 中的图片链接为本地路径

使用方法：
    python main.py
"""
import os
import re
import shutil
from datetime import datetime
from typing import Dict, List, Tuple, Optional

from config import (
    BASE_DIR, POSTS_DIR, IMAGES_DIR, DATA_FILE,
    IMAGE_PATTERN
)
from scanner import scan_all_posts
from downloader import download_images_for_post
from replacer import replace_image_links


def load_csdn_mapping() -> Dict[str, str]:
    """
    加载 CSDN 文章映射关系
    
    Returns:
        Dict[str, str]: {文章文件名：CSDN URL}
    """
    mapping = {}
    
    if not os.path.exists(DATA_FILE):
        print(f"警告：数据文件不存在：{DATA_FILE}")
        return mapping
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # 格式：URL : 文章标题
            if ' : ' in line:
                url, title = line.split(' : ', 1)
                # 将标题转换为文件名（加 .md 后缀）
                filename = title + '.md'
                mapping[filename] = url.strip()
                print(f"映射：{filename} -> {url}")
    
    return mapping


def find_matching_post(filename: str, csdn_mapping: Dict[str, str]) -> Optional[str]:
    """
    找到文章对应的 CSDN URL
    
    由于文件名可能和 data.md 中的标题不完全一致，需要进行匹配
    """
    # 直接匹配
    if filename in csdn_mapping:
        return csdn_mapping[filename]
    
    # 尝试去掉 .md 后缀匹配
    filename_no_ext = filename.replace('.md', '')
    for key, url in csdn_mapping.items():
        if filename_no_ext in key or key.replace('.md', '') in filename_no_ext:
            return url
    
    return None


def backup_posts() -> Optional[str]:
    """
    备份文章目录
    
    Returns:
        str: 备份目录路径
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(BASE_DIR, f"source/_posts_backup_{timestamp}")
    
    try:
        shutil.copytree(POSTS_DIR, backup_dir)
        print(f"[OK] 已备份文章目录：{backup_dir}")
        return backup_dir
    except Exception as e:
        print(f"[FAIL] 备份失败：{e}")
        return None


def get_unique_images(posts_images: Dict[str, List[Dict]]) -> Dict[str, List[str]]:
    """
    获取每篇文章的唯一图片 URL 列表（去重，保持顺序）
    
    Returns:
        Dict[str, List[str]]: {文章文件名：唯一 URL 列表}
    """
    result = {}
    
    for filename, images in posts_images.items():
        seen = set()
        unique_urls = []
        
        for img in images:
            url = img['url']
            if url not in seen:
                seen.add(url)
                unique_urls.append(url)
        
        result[filename] = unique_urls
    
    return result


def main():
    """主函数"""
    print("=" * 60)
    print("博客图片迁移工具")
    print("=" * 60)
    print(f"文章目录：{POSTS_DIR}")
    print(f"图片目录：{IMAGES_DIR}")
    print()
    
    # 步骤 1：创建图片目录
    print("【步骤 1】创建图片目录...")
    os.makedirs(IMAGES_DIR, exist_ok=True)
    print(f"[OK] 图片目录已创建：{IMAGES_DIR}")
    print()
    
    # 步骤 2：加载 CSDN 映射
    print("【步骤 2】加载 CSDN 文章映射...")
    csdn_mapping = load_csdn_mapping()
    print(f"[OK] 加载了 {len(csdn_mapping)} 个 CSDN 文章映射")
    print()
    
    # 步骤 3：扫描文章中的图片
    print("【步骤 3】扫描文章中的外部图片链接...")
    posts_images = scan_all_posts()
    
    if not posts_images:
        print("未发现需要处理的图片")
        return
    
    total_images = sum(len(imgs) for imgs in posts_images.values())
    print(f"\n[OK] 扫描完成：{len(posts_images)} 篇文章，{total_images} 张外部图片")
    print()
    
    # 步骤 4：备份文章
    print("【步骤 4】备份文章目录...")
    backup_dir = backup_posts()
    print()
    
    # 步骤 5：下载图片
    print("【步骤 5】下载图片到本地...")
    url_mapping = {}  # {文章文件名：{原 URL: 本地路径}}
    
    total_posts = len(posts_images)
    for i, (filename, images) in enumerate(posts_images.items(), 1):
        print(f"\n进度：[{i}/{total_posts}]")
        # 获取唯一 URL 列表（去重）
        unique_images_list = get_unique_images({filename: images})[filename]
        
        # 下载图片
        post_name = filename.replace('.md', '')
        mapping = download_images_for_post(post_name, images)
        url_mapping[filename] = mapping
    
    print()
    
    # 步骤 6：替换链接
    print("【步骤 6】替换 Markdown 中的图片链接...")
    total_replaced = 0
    
    for filename, mapping in url_mapping.items():
        file_path = os.path.join(POSTS_DIR, filename)
        if os.path.exists(file_path):
            count = replace_image_links(file_path, mapping)
            if count > 0:
                print(f"[OK] {filename}: 替换 {count} 个图片链接")
                total_replaced += count
    
    print()
    
    # 完成
    print("=" * 60)
    print("迁移完成！")
    print("=" * 60)
    print(f"图片目录：{IMAGES_DIR}")
    print(f"替换链接：{total_replaced} 个")
    if backup_dir:
        print(f"备份目录：{backup_dir}")
    print()
    print("下一步：")
    print("1. 运行 npm run server 预览博客")
    print("2. 检查所有图片是否正常显示")
    print("3. 确认无误后可以删除备份目录")


if __name__ == "__main__":
    main()
