# 创建时间：2021/6/1 8:20
from sys import argv

file = argv[1]

with open(file) as file_object:
    lines = file_object
    s = 0
    for line in lines:
        if line.startswith(">"):
            if s != 0:
                print(s)
            s = 0
            print(line.rstrip(), end="\t")
        else:
            s += len(line.rstrip())
    print(s)


file_object.close()