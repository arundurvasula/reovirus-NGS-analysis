import csv
import sys
import re
from collections import Counter
filename = sys.argv[1]
sample = sys.argv[2]
result = {}
DESC_START = 6 #description start
CTG_NAME = 0
CTG_LEN = 1

with open(filename, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		if row[CTG_NAME] not in result:
			if '[' in row[DESC_START]:
				species=row[DESC_START].split('[', 1)[1].split(']')[0]
			elif '[' in row[DESC_START+1]:
				species=row[DESC_START+1].split('[', 1)[1].split(']')[0]
			else:
				species=None
			try:
				result[row[CTG_NAME]] = [row[CTG_LEN], species.lower()]
			except:
				pass

#result: { contig: [length, species]
# constants referring to indexes in result:
LEN = 0
SPECIES = 1
#counts:{ species: [# contigs, min length, max length] }
# constants referring to indexes in counts:
NUM_CTGS = 0
counts = {}
for contig in result:
	try:
		counts[result[contig][SPECIES]].append(contig)
	except KeyError:
		counts[result[contig][SPECIES]] = [contig] 

virus_contigs = open("../results/" + sample + "/contigs/virus_contig.fa", 'r')
for key in counts:
	tempfile = open("../temp/" + sample + "/contigs" + key.replace(" ", "") + ".txt", 'w')
	tempfile.writelines("%s\n" % item  for item in counts[key])
