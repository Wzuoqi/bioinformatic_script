# 创建时间：2021/5/27 14:58
from sys import argv

file = argv[1]
database = './Cl_backgroud_file.txt'

id_list = []
final_list = []
with open(file) as file_object:
    lines = file_object
    for line in lines:
        id_list.append(line)
file_object.close()

with open(database) as data_object:
    datas = data_object
    for data in datas:
        list2 = data.split('\t')
        a = list2[0]+'\n'
        if a in id_list:
            final_list.append(data)
        else:
            continue
final_list.sort()
for x in final_list:
    print(x.rstrip())

data_object.close()

