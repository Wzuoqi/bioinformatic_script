# 创建时间：2021/5/27 14:58
from sys import argv

file = argv[1]

with open(file) as file_object:
    lines = file_object
    flag = False
    dict1 = {}
    s = ""
    a = ""
    for line in lines:
        if line.startswith('>'):
            a = s[4873:4876]
            # 切片位置
            print(a.rstrip())
            print(line.rstrip())
            s = ""
        else:
            s += line
    a = s[4873:4876]
    # 额外做一次切片
    print(a.rstrip())
file_object.close()
