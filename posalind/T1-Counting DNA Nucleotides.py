# 创建时间：2022/3/31 13:57
def count_nt(s):
    dict = {x:0 for x in 'ACGT'}
    for nt in s:
        if nt in 'ACGT':
            dict[nt] += 1
    return [j for i,j in dict.items()]

path = "D:\download\\rosalind_dna (2).txt"
with open(path) as fp:
    seq = fp.readline().strip("/n")
    print(count_nt(seq))
