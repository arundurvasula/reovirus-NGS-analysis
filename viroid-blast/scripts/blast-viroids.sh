#!/bin/bash
source ~/.bashrc
blast_threads=2
#contigs=(`find ../data/contigs/*.fa -type f`)
contigs=(../data/contigs/LR106-contig.fa)
for file in ${contigs[@]}
do
    sample=${file##*/}
    time blastn -db /home/arun/Documents/NGS-summary-report/viroid-blast/data/refseq/viroids.nucl -query $file -evalue 10 -word_size 4 -gapopen 2 -gapextend 2 -max_target_seqs 3 -outfmt "10 qseqid qlen sseqid evalue bitscore sskingdoms stitle sblastnames salltitles scomnames sscblyinames" -out ../results/$sample-blast.csv -num_threads $blast_threads &
done
