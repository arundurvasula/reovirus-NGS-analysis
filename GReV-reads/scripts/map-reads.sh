#!/bin/bash
source ~/.bashrc

refseq=../data/refseq/GReV.txt

bwa index -a bwtsw $refseq
bwa bwasw $refseq ../data/trimmed-unmapped/LV89_1-1.fa > ../temp/alignment.sam
samtools view -bS -F 4 ../temp/alignment.sam > ../temp/aln.bam
samtools sort ../temp/aln.bam ../temp/aln.sorted
samtools index ../temp/aln.sorted.bam
genomeCoverageBed -ibam ../temp/aln.sorted.bam -g $refseq -d -max 1 > ../temp/coverageHist.txt
awk 'BEGIN {count=0} $3 != 0 {count += 1} END {print (count/NR)*100}' ../temp/coverageHist.txt > ../temp/coverage.txt
