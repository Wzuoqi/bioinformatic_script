# 创建时间：2021/5/27 10:54
from tkinter.filedialog import askopenfilename
import sys
from pprint import pprint

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


sys.stdout = Logger('chr31.gff3')
# 将结果保存在output.gff3中

with open(file) as file_object:
    lines = file_object
    list2 = \
        [0, 56882, 154168, 284771, 640873, 727867, 866672, 982325, 1107459, 1261686, 1284977, 1321197, 1429561, 1440593,
         1474636, 1512466, 1531158, 1556439, 1572737, 1597007, 1651443, 1659758, 1734516, 1819798, 1840529, 1919526,
         1934592, 1958696, 1975163, 1979626, 2000118, 2028459, 2053293, 2060940, 2076877, 2125017, 2138433, 2142335,
         2186684, 2218460, 2230063, 2242304]

    # list2获取各个scaffold的序号增加量

    for line in lines:
        list1 = line.split('\t')
        a = int(list1[3])
        # a为起始位点
        b = int(list1[4])
        # b为终止位点
        str_id = list1[0]
        seq_str = 'scaffold'
        head, sep, tail = str_id.partition(seq_str)
        scaffold_id = int(tail)
        a += list2[scaffold_id - 1]
        b += list2[scaffold_id - 1]
        list1[3] = a
        list1[4] = b
        list1[0] = 'chr31'
        print(*list1, sep='\t')


file_object.close()
