"""
下载模块：从 CSDN 下载图片
"""
import requests
import os
import time
from typing import List, Dict
from config import HEADERS, TIMEOUT, MAX_RETRIES, IMAGES_DIR

# 创建全局 Session 以提高效率
_session = None

def get_session():
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update(HEADERS)
    return _session


def download_image(url: str, save_path: str, delay: float = 0.1) -> bool:
    """
    下载单张图片
    
    Args:
        url: 图片 URL
        save_path: 保存路径
        delay: 下载前延迟时间（秒），避免触发反爬
    
    Returns:
        bool: 是否下载成功
    """
    # 如果文件已存在，跳过
    if os.path.exists(save_path):
        print(f"  [SKIP] 已存在：{save_path}")
        return True
    
    # 延迟一下，避免触发反爬
    time.sleep(delay)
    
    session = get_session()
    
    print(f"  [INFO] 开始下载：{url[:50]}...")
    
    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            
            # 确保目录存在
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            print(f"  [OK] 下载：{save_path}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"  [FAIL] 下载失败 (尝试 {attempt + 1}/{MAX_RETRIES}): {url}")
            print(f"    错误：{e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(1)  # 等待 1 秒后重试
    
    return False


def get_image_extension(url: str) -> str:
    """
    从 URL 获取图片扩展名
    """
    # 从 URL 中提取文件名
    filename = url.split('/')[-1].split('?')[0]
    
    # 常见图片扩展名
    extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg']
    
    for ext in extensions:
        if filename.lower().endswith(ext):
            return ext
    
    # 默认返回 .png
    return '.png'


def download_images_for_post(
    post_name: str,
    images: List[Dict],
    csdn_url: str = None
) -> Dict[str, str]:
    """
    下载单篇文章的所有图片
    
    Args:
        post_name: 文章文件名（不含.md）
        images: 图片信息列表
        csdn_url: CSDN 文章 URL（用于构造图片链接）
    
    Returns:
        Dict[str, str]: {原 URL: 本地路径} 映射
    """
    result = {}
    
    # 创建文章对应的图片目录
    post_image_dir = os.path.join(IMAGES_DIR, post_name)
    os.makedirs(post_image_dir, exist_ok=True)
    
    # 去重，保持顺序
    seen_urls = set()
    unique_images = []
    for img in images:
        if img['url'] not in seen_urls:
            seen_urls.add(img['url'])
            unique_images.append(img)
    
    print(f"\n下载文章图片：{post_name} ({len(unique_images)} 张)")
    
    for idx, img_info in enumerate(unique_images, 1):
        url = img_info['url']
        
        # 获取扩展名
        ext = get_image_extension(url)
        
        # 生成新文件名（按序号）
        new_filename = f"{idx}{ext}"
        save_path = os.path.join(post_image_dir, new_filename)
        
        # 下载图片
        if download_image(url, save_path):
            # 构建本地访问路径（用于替换 Markdown 中的链接）
            local_path = f"/source/images/{post_name}/{new_filename}"
            result[url] = local_path
        else:
            print(f"  [WARN] 跳过：{url}")
    
    return result


if __name__ == "__main__":
    # 测试下载
    test_url = "https://i-blog.csdnimg.cn/direct/30014f5b67414420badd1675c1ee451c.png"
    test_path = os.path.join(IMAGES_DIR, "test", "1.png")
    
    print(f"测试下载：{test_url}")
    success = download_image(test_url, test_path)
    print(f"结果：{'成功' if success else '失败'}")
