# 创建时间：2022/5/12 15:22
def Consensus(s: str):
    with open(s) as file:
        base = 'ACGT'
        n = 4
        seqs = [line.strip() for line in file if line[0] != '>']
        print(seqs[0])
        res = ''
        m = len(seqs[0])
        ref = [[0] * m for _ in range(n)]
        for j in range(m):
            max_ = -1
            for i in range(n):
                ref[i][j] = [seq[j] for seq in seqs].count(base[i])
                if max_ < ref[i][j]:
                    max_ = ref[i][j]
                    nt = base[i]
            res += nt
        return res, ref
    file.close()


x = './output.fasta'
print(Consensus(x))

