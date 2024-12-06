# python function_anno.py target.anno.pep.fa uniprot_map.id blast_map.id > result.anno.pep.fa

from sys import argv

old_gff = argv[1]
uniprot_mapID = argv[2]
blast_mapID = argv[3]

uniprot_dict = {}
blast_dict = {}

with open(uniprot_mapID) as file_object:
    lines = file_object
    for line in lines:
        uniprot_dict[line.split(" ")[0]] = line.split(" ")[1:]
file_object.close()

with open(blast_mapID) as file_object:
    lines = file_object
    for line in lines:
        blast_dict[line.split()[1]] = line.split()[0]
file_object.close()



file = old_gff
with open(file) as file_object:
    lines = file_object
    for line in lines:
        if line.startswith('>'):
            print(s.rstrip())
            s = ""
            print(line.rstrip())
        else:
            s += line.rstrip()
file_object.close()