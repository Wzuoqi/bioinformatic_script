# python function_anno.py target.anno.pep.fa uniprot_map.id blast_map.id > result.anno.pep.fa

from sys import argv

old_gff = argv[1]
uniprot_mapID = argv[2]
blast_mapID = argv[3]

with open(uniprot_mapID) as file_object:
    lines = file_object
file_object.close()



file = old_gff
with open(file) as file_object:
    lines = file_object
    s = ""
    for line in lines:
        if line.startswith('>'):
            print(s.rstrip())
            s = ""
            print(line.rstrip())
        else:
            s += line.rstrip()
    print(s.rstrip())
file_object.close()