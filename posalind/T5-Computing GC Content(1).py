# 创建时间：2022/4/4 23:26
def gc(path):
    with open(path) as fp:
        seqs = []
        names = []
        res = ''
        for f in fp:
            f = f.strip()
            if f[0] == '>':
                names.append(f)
                seqs.append(res)
                res = ''
            else:
                res += f
        seqs.append(res)
    return count_gc(names, seqs[1:])


def count_gc(names, seqs):
    count_gc = [round(sum(1 for nt in s if nt in 'GC') / len(s), 6) for s in seqs]
    res = [(i, j) for i, j in zip(names, count_gc)]
    return max(res, key=lambda x: x[1])


print(gc(r'D:\download\rosalind_gc (4).txt'))
