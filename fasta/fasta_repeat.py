# 创建时间：2021/6/1 8:20
from sys import argv

file = argv[1]

with open(file) as file_object:
    lines = file_object
    fasta_string = ""
    list1 = []
    title = ""
    flag = False
    for line in lines:
        if line.startswith(">"):
            if fasta_string in list1:
                fasta_string = ""
            else:
                list1.append(fasta_string)
                print(fasta_string)
                print(line)
                fasta_string = ""
        else:
            fasta_string += line

    if fasta_string in list1:
        print(fasta_string)

file_object.close()

nohup singularity exec ~/04_docker/braker3.sif braker.pl --genome=GCA_030704895.1_SYSU_HVIGI_v1.0_genomic.fna --species=GCA_030704895 --min_contig=5000 --prot_seq=/home/wangzuoqi/02_dataset/02_masked_genome/proteins.fasta --threads=12 --gff3 --workingdir=GCA_030704895 --useexisting &