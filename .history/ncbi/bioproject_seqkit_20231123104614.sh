#!/bin/bash

# 从文件中读取数据
input_file="bioproject"

# 按空行分隔数据块
IFS=$'\n\n'

# 遍历每个数据块
for data_block in $(cat "$input_file"); do
    # 提取项目编号
    project_number=$(echo "$data_block" | grep -oP '^\d+')

    # 提取项目名称
    project_name=$(echo "$data_block" | grep -oP '\d+\.\s(.+)$' | sed 's/^\s*//')

    # 提取Organism
    organism=$(echo "$data_block" | grep -oP 'Organism: \K.*')

    # 提取Taxonomy ID
    taxonomy_id=$(echo "$data_block" | grep -oP 'Taxonomy ID \K\d+')

    # 提取BioProject Accession
    bio_project=$(echo "$data_block" | grep -oP 'BioProject Accession: \K.*')

    # 提取ID
    id=$(echo "$data_block" | grep -oP 'ID: \K.*')

    # 输出按照指定格式
    echo -e "$project_number\t$project_name\t$organism\t$taxonomy_id\t$bio_project\t$id"
done
