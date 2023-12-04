# usage: python genome_clean genome.fa
# output: genome.fa.clean
from sys import argv

inputFile = open(argv[1],'r').readlines()
outputName = argv[1]+'.clean'
outputFile = open(outputName, 'w')

seqDict = {}

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

