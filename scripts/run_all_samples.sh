#!/bin/bash
allsamples=(`find ../data/trimmed-unmapped/* -type f`)

for sample in "${allsamples[@]}"
do
    y=${sample%.*}
    samplename=${y##*/}
    if [ "$samplename" == "LV-89-02-trimmed-unmapped" ]; then
	continue
    fi
    if [ "$samplename" == "LR-102-trimmed-unmapped" ]; then
	continue
    fi
    if [ "$samplename" == "CB-100-trimmed-unmapped" ]; then
	continue
    fi

    bash $samplename.sh
done
