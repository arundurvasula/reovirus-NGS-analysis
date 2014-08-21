allsamples=(`find ../data/trimmed-unmapped/* -type f`)

for sample in "${allsamples[@]}"
do
    y=${sample%.*}
    samplename=${y##*/}
    bash new_sample.sh $samplename
done
