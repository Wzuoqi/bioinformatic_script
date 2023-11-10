# 创建时间：2022/3/31 14:26
def rna(path):
    with open(path) as fp:
        seq = fp.readline()
    return translate_RNA(seq)


def translate_RNA(seq):
    return ''.join(['U' if s == 'T' else s for s in seq])


print(rna(r'D:\download\rosalind_rna.txt'))
