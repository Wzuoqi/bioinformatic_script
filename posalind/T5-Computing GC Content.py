# 创建时间：2022/4/4 23:26
from tkinter.filedialog import askopenfilename
import sys


def count_CG(s):
    num = 0
    for nt in s:
        if nt in 'CG':
            num += 1
    return round(num / len(s) * 100, 6)


file = askopenfilename()
with open(file) as file_object:
    lines = file_object
    cg_dict = {}
    for line in lines:
        if line.startswith(">"):
            name = line[1:].rstrip()
            cg_dict[name] = 0
        else:
            cg_dict[name] += count_CG(line)
        # max_seq = max(cg_dict, key=lambda x: x[1])
        # print(max_seq)
        # print(cg_dict.get(max_seq))
    for key in cg_dict:
        print(key)
        print(cg_dict[key])
