'''
Author: midjuly7 wangzuoqi@zju.edu.cn
Date: 2024-03-15 16:45:53
LastEditors: midjuly7 wangzuoqi@zju.edu.cn
LastEditTime: 2024-03-15 16:49:46
FilePath: \fasta\function_anno.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# python function_anno.py target.anno.pep.fa uniprot_map.id blast

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