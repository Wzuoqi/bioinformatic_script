import requests
import xml.etree.ElementTree as ET
import sys


def get_taxonomy_info(species_name):
    # 通过物种名搜索 NCBI Taxonomy 数据库
    search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term={species_name}[Scientific Name]&retmode=xml"
    search_response = requests.get(search_url)
    search_tree = ET.fromstring(search_response.content)

    error_list = search_tree.find("ErrorList")
    if error_list is not None:
        return f"No taxonomy information found for {species_name}"

    tax_id = search_tree.find("IdList/Id").text

    # 通过 Taxonomy ID 获取分类信息
    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id={tax_id}&retmode=xml"
    fetch_response = requests.get(fetch_url)
    fetch_tree = ET.fromstring(fetch_response.content)

    # 解析分类信息
    taxonomy_info = {
        "organism": species_name,
        "class": "",
        "subclass": "",
        "infraclass": "",
        "cohort": "",
        "superorder": "",
        "order": "",
        "suborder": "",
        "infraorder": "",
        "parvorder": "",
        "superfamily": "",
        "family": "",
        "subfamily": "",
        "tribe": "",
        "subtribe": "",
        "genus": ""
    }

    for taxon in fetch_tree.iter("Taxon"):
        rank = taxon.find("Rank").text.lower()
        name = taxon.find("ScientificName").text
        if rank in taxonomy_info:
            taxonomy_info[rank] = name

    return taxonomy_info


# 从命令行参数读取物种名文件路径
species_file = sys.argv[1]

# 从文件中读取物种名
with open(species_file, 'r') as file:
    species_list = [line.strip() for line in file]

for species_name in species_list:
    taxonomy_info = get_taxonomy_info(species_name)
    if isinstance(taxonomy_info, dict):
        print(f"{taxonomy_info['organism']}\t{taxonomy_info['class']}\t{taxonomy_info['subclass']}\t{taxonomy_info['infraclass']}\t{taxonomy_info['cohort']}\t{taxonomy_info['superorder']}\t{taxonomy_info['order']}\t{taxonomy_info['suborder']}\t{taxonomy_info['infraorder']}\t{taxonomy_info['parvorder']}\t{taxonomy_info['superfamily']}\t{taxonomy_info['family']}\t{taxonomy_info['subfamily']}\t{taxonomy_info['tribe']}\t{taxonomy_info['subtribe']}\t{taxonomy_info['genus']}")
    else:
        print(taxonomy_info)
