#!/bin/bash
#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"
FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1-lunch
SAMPLE_PREFIX=SRR072
GENOME_DIR=/Users/cmdb/data/genomes
RESULT_DIR=dmel5
ANNOTATION=dmel-all-r5.57.gff
CORES=4

for i in 893
do
  fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  tophat -p 4 -G $OUTPUT_DIR/$ANNOTATION -o $RESULT_DIR $GENOME_DIR/dmel-all-chromosome-r5.57 $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz
  cufflinks -p 4 -G $OUTPUT_DIR/$ANNOTATION -o $RESULT_DIR $RESULT_DIR/accepted_hits.bam
done