# 创建时间：2021/9/28 17:05
from sys import argv
import re

file = argv[1]

with open(file) as file_object:
    lines = file_object
    t = ''
    title = ''
    key_string = ''
    test_string = ''
    key = re.compile('RGC*.{5}C') # 只需要在这里改正则表达式即可
    for line in lines:
        if line.startswith('>'):
            test_string = re.search(key, t)
            if test_string is not None:
                key_string = key.search(t).group()
                print(title.rstrip())
                print(key_string)
            title = line
            t = ''
        else:
            t += line
    test_string = re.search(key, t)
    if test_string is not None:
        key_string = key.search(t).group()
        print(title.rstrip())
        print(key_string)
file_object.close()
