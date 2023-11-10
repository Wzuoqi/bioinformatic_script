# 创建时间：2021/5/27 14:58
from sys import argv

file = argv[1]

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
