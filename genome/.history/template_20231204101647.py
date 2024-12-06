# usage: python template.py genome.fa
# output: genome.fa.xxx
from sys import argv

inputFile = open(argv[1], 'r').readlines()
outputName = argv[1]+'.xxx'
outputFile = open(outputName, 'w')

seqDict = {} # 用于

for line in inputFile:
    line = line.rstrip()
    if line.startswith('>'):
        seqName = line.split()[0]
        seqDict[seqName] = []
    else:
        seqDict[seqName].append(line)

for seqKey in seqDict:
    outputFile.write(seqKey + '\n')
    outputFile.write(''.join(seqDict[seqKey]) + '\n')

outputFile.close()
