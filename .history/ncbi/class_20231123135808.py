# 从ncbi的taxonomy数据库中提取物种的纲目属分类信息

from sys import  argv

order=''
family=''
genus=''
for x in open(argv[1]):
    if len(x.split('-',1)[0]) == 1:
        order = x.split('-',1)[1]
    elif len(x.split('-',1)[0]) == 3:
        family = x.split('-',1)[1]
    elif len(x.split('-',1)[0]) == 5:
        genus = x.split('-',1)[1]
    elif len(x.split('-',1)[0]) == 7:
        print(order.strip()+'\t'+family.strip()+'\t'+genus.strip()+'\t'+x.split('-',1)[1].strip())
    else:
        continue