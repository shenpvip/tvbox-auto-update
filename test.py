import os
import requests
import zipfile

def download_and_extract_github_repo(repo_url, save_dir="downloaded_repo"):
    """
    下载指定 GitHub 仓库的 ZIP 文件并解压缩到指定目录。

    :param repo_url: GitHub 仓库 URL，例如 "https://github.com/user/repo"
    :param save_dir: 解压目标目录，默认为 "downloaded_repo"
    """
    
    # 下载 ZIP 文件
    print(f"正在下载仓库 ZIP 文件：{repo_url}")
    response = requests.get(repo_url, stream=True)
    if response.status_code == 200:
        zip_file_path = "repo.zip"
        with open(zip_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("下载完成。")
    else:
        print(f"下载失败，HTTP 状态码：{response.status_code}")
        return

    # 解压 ZIP 文件
    os.makedirs(save_dir, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(save_dir)
    print(f"解压完成，文件已保存到：{os.path.abspath(save_dir)}")

    # 删除临时 ZIP 文件
    os.remove(zip_file_path)

# 示例：下载并解压
repo_url = "https://github.com/fish2018/PG/raw/main/pg.20241129-0204.zip"  # 替换为目标仓库地址
download_and_extract_github_repo(repo_url)
