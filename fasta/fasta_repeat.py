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