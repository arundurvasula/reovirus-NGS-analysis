import csv
import sys
import re
from collections import Counter
filename = sys.argv[1]
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

#== really bad code below ==#
## code counts the number of species and gets the min and max length of the contigs

#result: { contig: [length, species]
# constants referring to indexes in result:
LEN = 0
SPECIES = 1
#counts:{ species: [# contigs, min length, max length] }
# constants referring to indexes in counts:
NUM_CTGS = 0
MIN = 1
MAX = 2
counts = {}
for contig in result:
	current_species = result[contig][SPECIES]
	try:
		counts[current_species][0] += 1
		if int(result[contig][LEN]) < counts[current_species][MIN]:
			counts[current_species][MIN] = int(result[contig][LEN])
		if int(result[contig][LEN]) > counts[current_species][MAX]:
			counts[current_species][MAX] = int(result[contig][LEN])
	except KeyError:
		counts[current_species] = [1, int(result[contig][LEN]),  int(result[contig][LEN])] 

outfile = open(filename+".counts.lengths.csv", 'w')
csvwriter = csv.writer(outfile, delimiter=",")
csvwriter.writerow(["Virus", "# of contigs", "min contig", "max contig"])
for key, value in counts.iteritems():
    csvwriter.writerow([key, value[0], value[1], value[2]])
