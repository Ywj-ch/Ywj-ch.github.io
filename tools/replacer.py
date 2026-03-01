"""
替换模块：将 Markdown 中的图片链接替换为本地路径
"""
import re
import os
from typing import Dict, List
from config import POSTS_DIR, IMAGE_PATTERN


def replace_image_links(file_path: str, url_to_path: Dict[str, str]) -> int:
    """
    替换单个文件中的图片链接
    
    Args:
        file_path: Markdown 文件路径
        url_to_path: {原 URL: 本地路径} 映射
    
    Returns:
        int: 替换的数量
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replace_count = 0
    
    # 遍历所有需要替换的 URL
    for url, local_path in url_to_path.items():
        # 匹配所有使用这个 URL 的图片
        pattern = r'!\[([^\]]*)\]\(' + re.escape(url) + r'\)'
        replacement = f'![\\1]({local_path})'
        
        matches = list(re.finditer(pattern, content))
        if matches:
            content = re.sub(pattern, replacement, content)
            replace_count += len(matches)
    
    # 只有内容发生变化才写入
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return replace_count


def replace_all_posts(url_mapping: Dict[str, Dict[str, str]]) -> int:
    """
    替换所有文章的图片链接
    
    Args:
        url_mapping: {文章文件名：{原 URL: 本地路径}}
    
    Returns:
        int: 总共替换的数量
    """
    total = 0
    
    for filename, mapping in url_mapping.items():
        file_path = os.path.join(POSTS_DIR, filename)
        
        if os.path.exists(file_path):
            count = replace_image_links(file_path, mapping)
            if count > 0:
                print(f"[OK] {filename}: 替换 {count} 个图片链接")
                total += count
        else:
            print(f"[FAIL] 文件不存在：{file_path}")
    
    return total


if __name__ == "__main__":
    print("替换模块测试")
