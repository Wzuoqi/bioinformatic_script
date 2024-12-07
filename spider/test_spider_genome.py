import requests
from bs4 import BeautifulSoup
import re

def get_assembly_name(genome_id):
    """
    第一步：从NCBI FTP网站获取Assembly名称
    """
    # 处理基本ID和构建FTP URL
    genome_base = genome_id.split('.')[0]
    number = genome_base.split('_')[1]

    # 构建分段路径
    path_parts = [
        number[:3],
        number[3:6],
        number[6:9]
    ]

    # 构建FTP目录URL
    ftp_url = f"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/{'/'.join(path_parts)}"

    try:
        response = requests.get(ftp_url)
        response.encoding = "utf-8"

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找包含assembly名称的链接
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and genome_id in href:
                # 提取assembly名称 (例如：ASM14701v1)
                match = re.search(rf'{genome_id}_([^/]+)/?$', href)
                if match:
                    return match.group(1)

        return None

    except Exception as e:
        print(f"Error fetching assembly name for {genome_id}: {str(e)}")
        return None

def generate_download_link(genome_id, assembly_name):
    """
    第二步：根据genome_id和assembly_name生成下载链接
    """
    # 处理基本ID
    genome_base = genome_id.split('.')[0]
    number = genome_base.split('_')[1]

    # 构建分段路径
    path_parts = [
        number[:3],
        number[3:6],
        number[6:9]
    ]

    # 构建完整的下载链接
    full_name = f"{genome_id}_{assembly_name}"
    ftp_path = f"https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/{'/'.join(path_parts)}/{full_name}"
    download_link = f"{ftp_path}/{full_name}_genomic.fna.gz"

    return download_link

def process_file(input_file, output_file):
    """
    处理输入文件并生成下载链接
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            genome_id = line.strip()  # 移除换行符和空白字符
            if genome_id:  # 确保不是空行
                # 第一步：获取assembly名称
                assembly_name = get_assembly_name(genome_id)
                if assembly_name:
                    # 第二步：生成下载链接
                    download_link = generate_download_link(genome_id, assembly_name)
                    outfile.write(f"{genome_id}\t{download_link}\n")
                else:
                    outfile.write(f"{genome_id}\tFailed to get assembly name\n")

if __name__ == "__main__":
    input_file = "GCA_name.id"
    output_file = "GCA_download_links.txt"
    process_file(input_file, output_file)
    print(f"下载链接已生成并保存到 {output_file}")