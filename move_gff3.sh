#!/usr/bin/env bash

# Make sure that at least one ID is provided as an argument
if [ $# -eq 0 ]
then
    echo "Error: No ID provided. Please provide at least one ID as an argument."
    exit 1
fi

# Loop through all the IDs provided as arguments
for ID in "$@"
do
    ID_without_suffix=${ID%.hisat2.sorted.bam}
    # Find the folder with "output_" and the ID in its name on the remote server
    output_folder=$(ssh dl380no3 "find /home/negar/projects/spladd_single_mode -name "output_$ID"")

    # Copy the .gff3 file from the remote server
    scp negar@dl380no3:$output_folder/merge_graphs_exon_skip_C3.confirmed.gff3 ./IGV_inputs/$ID

    # Rename the .gff3 file to ID_without_suffix_merge_graphs_exon_skip_C3.confirmed.gff3
    mv merge_graphs_exon_skip_C3.confirmed.gff3 $ID_without_suffix_exon_skip_C3.confirmed.gff3


done
