# 创建时间：2021/5/27 14:58
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


sys.stdout = Logger('output.fasta')
# 将结果保存在output.fasta中

with open(file) as file_object:
    lines = file_object
    gene_length = []
    for line in lines:
        s = line.split('\t')
        if s[1] == 'intron':
            x = int(s[3]) - int(s[2])
            gene_length.append(x)
        else:
            continue
    total_length = 0
    for i in gene_length:
        total_length += i
    average_gene_length = total_length / len(gene_length)
    print(average_gene_length)
    print(len(gene_length))

file_object.close()
