#!/bin/bash
#load path from .bash_profile
source /home/arun/.bash_profile

SAMPLE=$1
cp ./LV-89-02-trimmed-unmapped.sh ./temp.$SAMPLE.sh
sed s/sample\=\'LV-89-02-trimmed-unmapped\'/sample\=\'$SAMPLE\'/ <temp.$SAMPLE.sh >$SAMPLE.sh
rm temp.$SAMPLE.sh
mkdir ../temp/$SAMPLE
mkdir ../results/$SAMPLE/
mkdir ../results/$SAMPLE/blast ../results/$SAMPLE/contigs ../results/$SAMPLE/coverage ../results/$SAMPLE/reads
