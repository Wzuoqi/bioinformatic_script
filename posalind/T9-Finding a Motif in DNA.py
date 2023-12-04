# 创建时间：2022/5/7 9:11
def motif_search(s: str, target: str):
    s_length = len(s)
    target_length = len(target)
    i, j = 0, 0
    ret = []
    for i in range(s_length - target_length + 1):
        if s[i:i+target_length] == target:
            ret.append(i+1)
    return ret


x = 'GCTTTTCGCGGGTTTTCGCTTTTCGCACAGCACTGACTGGATTTTCGCTTTTCGCTAATCTTTTCGCGTTTTCGCGTTGTTTTCGCACGCAATTTTCGCTGGTTTTCGCAGTTTTTCGCTATTTTCGCCCTTTTCGCGTTTTCGCTGGCAATTTTCGCATTTTTCGCTATTTTCGCCTTTTCGCACCCAGCTTTTCGCTTTTCGCGTAAGGAGCATTCGCGATTTTCGCTTTTCGCACGTGTGCATTTTCGCGTTTTCGCTTTTCGCGTTTTTTCGCCTTTTCGCATTTTTCGCCGCGCAGAATTGTTAGTTTTTCGCATTTTCGCTTTTCGCGGTTTTCGCGTTTTTCGCGTTTTCGCGTTTTCGCGTTTTTCGCATTTTCGCGTCATTAGCGTTTTCGCGTTTTCGCTCTTTTCGCATTTTCGCGTGTTTTTCGCTTTTCGCATTTTCGCTGTAGGGTTTTCGCCATTTTTTTCGCATTTTCGCATTTTCGCTGTTTTCGCAATTTTCGCATTACGATTTTTCGCTTTTCGCAGTTTTCGCTCTTGTTTTCGCGTTTTCGCTTTTTTCGCACTCTACTTTTCGCCGGTAGGTTTTTCGCTTTTCGCATTTTCGCGTTTTCGCCTTTTCGCTTTTCGCTGGTGTTTTCGCCTTTTCGCTAGCAGTTTTCGCTTTTCGCGGTTTTCGCGGTTTTTCGCTTTTCGCTTTTCGCTAGGCAGGTGCCTTTTCGCTTTTCGCGCTTTTCGCGCCGACTTTTCGCTTTTCGCTTGTTTTCGCGCTTTTCGCATTTTCGCTTTTCGCGTGGTTTTCGCCCTTTTCGCAAGCATCCTTTTCGCGAGAAATTTTCGCTATTTTCGCTTTTCGCAAACCCTCGGGCCAGGTTTTCGCTTTTCGCGGGCTTTTCGCGTTAATTTTCGCGTTTTCGCCGCTTTTCGCGATTTTCGCCGCTTT'
y = 'TTTTCGCTT'
a = motif_search(x,y)
print(a)


