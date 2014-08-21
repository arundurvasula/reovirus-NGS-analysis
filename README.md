This folder contains scripts to analyze trimmed NGS data. This project will assemble sequence, run them through BLAST, and calculated coverage, number of contigs and read number for each virus of interest. To run a single new sample through, do the following:

	$ cd /scripts
	$ bash new_sample.sh <samplename>

It's also possible to do this for all samples in the trimmed-unmapped folder by running:

	$bash create_samples

which will find all files in the trimmed-unmapped directory and create folders for them. 

- Add the reference sequences to `/data/refseq/`
- Add the names of those viruses to a new file in `/data/virus-names/<samplename>.txt`
- Run the newly created script:

		$ cd /scripts
		$ bash <samplename>.sh
