# 创建时间：2021/7/29 20:08
#!/usr/bin/env python
# -*- coding: utf-8 -*-
tmp = open('2.txt', 'w')
with open('Melitaea_cinxia.gff3', 'r') as f:
    for line in f:
        if '#' not in line:
            line1 = line.strip().split()
            if line1[2] == 'mRNA':
                tmp.write(line.strip() + '\t@\t',)
            if line1[2] == 'exon':
                tmp.write(line.strip() + '\t@\t', )
        elif '###' in line:
            tmp.write('\n', )tmp.close()a = []for l in open('2.txt', 'r'):
    new_l = l.strip().split()
    a.append(new_l)a.sort(key=lambda x: (x[0], int(x[3]), int(x[4])))for i in a:
    for m in i:
        if '@' == m:
            print '\n',
        else:
            print m,