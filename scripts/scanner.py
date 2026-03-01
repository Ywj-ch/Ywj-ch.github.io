"""
扫描模块：提取 Markdown 文件中的图片链接
"""
import re
import os
from typing import Dict, List
from config import POSTS_DIR, IMAGE_PATTERN


def scan_post_file(file_path: str) -> List[Dict]:
    """
    扫描单个 Markdown 文件，提取所有图片链接
    
    Returns:
        List[Dict]: 图片信息列表，每个包含 {alt, url, line_no, match}
    """
    images = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用 finditer 获取所有匹配及其位置
    for match in re.finditer(IMAGE_PATTERN, content):
        alt = match.group(1)
        url = match.group(2)
        
        # 只处理外部图片链接（http 开头）
        if url.startswith('http'):
            # 计算行号
            line_no = content[:match.start()].count('\n') + 1
            images.append({
                'alt': alt,
                'url': url,
                'line_no': line_no,
                'match': match.group(0),  # 完整的 ![alt](url)
                'start': match.start(),
                'end': match.end()
            })
    
    return images


def scan_all_posts() -> Dict[str, List[Dict]]:
    """
    扫描所有博客文章
    
    Returns:
        Dict[str, List[Dict]]: {文章文件名：图片列表}
    """
    result = {}
    
    if not os.path.exists(POSTS_DIR):
        print(f"错误：文章目录不存在：{POSTS_DIR}")
        return result
    
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            file_path = os.path.join(POSTS_DIR, filename)
            images = scan_post_file(file_path)
            
            if images:
                result[filename] = images
                print(f"[OK] {filename}: 发现 {len(images)} 张图片")
            else:
                print(f"- {filename}: 无外部图片")
    
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("扫描博客文章中的图片链接")
    print("=" * 50)
    
    posts = scan_all_posts()
    
    total = sum(len(imgs) for imgs in posts.values())
    print(f"\n总计：{len(posts)} 篇文章，{total} 张外部图片")
