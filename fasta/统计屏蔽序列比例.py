# 创建时间：2021/5/27 14:58
from sys import argv

species = ""
file = argv[1]

with open(file) as file_object:
    lines = file_object
    large = 0
    small = 0
    for line in lines:
        if line.startswith('>'):
            continue
        else:
            for x in line:
                if x in "ATCG":
                    large += 1
                elif x in "atcg":
                    small += 1
                else:
                    continue
    print(large)
    print(small)
    ratio = round(small / (large + small) * 100, 2)
    print(ratio)
file_object.close()
