# 从ncbi中下载的bioproject summary中提取bioproject列表信息
import re

def extract_data(data_block):
    # 提取项目编号
    project_number_match = re.search(r'^\s*(\d+)', data_block)
    project_number = project_number_match.group(1) if project_number_match else ""

    # 提取项目名称
    project_name_match = re.search(r'^\s*\d+\.\s*(.+?)(?=\s*Organism:|$)', data_block)
    project_name = project_name_match.group(1).strip() if project_name_match else ""

    # 提取Organism
    organism_match = re.search(r'Organism: ([^(]+)', data_block)
    organism = organism_match.group(1).strip() if organism_match else ""

    # 提取Taxonomy ID
    taxonomy_id_match = re.search(r'Taxonomy ID (\d+)', data_block)
    taxonomy_id = taxonomy_id_match.group(1) if taxonomy_id_match else ""

    # 提取BioProject Accession
    bio_project_match = re.search(r'BioProject Accession: (\S+)', data_block)
    bio_project = bio_project_match.group(1) if bio_project_match else ""

    # 提取ID
    id_match = re.search(r'ID: (\d+)', data_block)
    id_value = id_match.group(1) if id_match else ""

    return f"{project_number}\t{project_name}\t{organism}\t{taxonomy_id}\t{bio_project}\t{id_value}"

# 从文件中读取数据
input_file = "./bioproject_result.txt"

# 打开文件并读取内容
with open(input_file, "r") as file:
    file_content = file.read()

# 按空行分隔数据块
data_blocks = re.split(r'\n\n', file_content)

# 输出表头
print("ProjectNumber\tProjectName\tOrganism\tTaxonomyID\tBioProjectAccession\tID")

# 遍历每个数据块并输出结果
for data_block in data_blocks:
    result = extract_data(data_block)
    print(result)
