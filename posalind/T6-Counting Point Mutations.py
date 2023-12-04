# 创建时间：2022/4/29 13:32
from tkinter.filedialog import askopenfilename
import sys


def count_HM_distance(x: str, y: str):
    x_len = len(x)
    y_len = len(y)
    HM_distance = 0
    if x_len != y_len:
        return "the length of consequence is not same "
    else:
        for i in range(len(x)):
            if x[i] != y[i]:
                HM_distance += 1

    return HM_distance


file = askopenfilename()
with open(file) as file_object:
    lines = file_object
    t = []
    for line in lines:
        t.append(line)
    print(count_HM_distance(t[0], t[1]))

file_object.close()
