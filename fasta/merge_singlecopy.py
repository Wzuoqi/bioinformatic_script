#usage
#python script.py seq_filename > mergeSeq.fasta

from sys import argv
from collections import defaultdict

seqDict = defaultdict(list)
currentSpecies = ""

with open(argv[1]) as input_file:
    for line in input_file:
    # build genome dict
        if line.startswith('>'):
            species = line.strip()[1:5]
            currentSpecies = species
        else:
            seqDict[currentSpecies].append(line.rstrip())

    for speciesName in seqDict:
        print('>'+speciesName)
        print(''.join(seqDict[speciesName]))












