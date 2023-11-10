# 创建时间：2022/3/31 14:31
def dna(path):
    with open(path) as fp:
        seq = fp.readline().rstrip()
    return complement(seq)


def complement(s):
    translate = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([translate[nt] for nt in s][::-1])


print(dna(r"D:\download\rosalind_revc.txt"))
