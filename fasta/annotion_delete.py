# 创建时间：2021/5/27 10:54
from tkinter.filedialog import askopenfilename
import sys

file = askopenfilename()


class Logger(object):
    """
    将文件运行中的输出部分保存到特定txt文件中
    """

    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('Onip_protein.fasta')
# 将结果保存在Onip_protein.fasta中

with open(file) as file_object:
    lines = file_object
    sep_str = "annotation:"
    for line in lines:
        if line.startswith('>'):
            head, sep, tail = line.partition(sep_str)
            print(head.rstrip())
        else:
            print(line.rstrip())
file_object.close()
