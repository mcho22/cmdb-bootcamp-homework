#!/bin/bash
#
# Day 1 - Homework: Part 2 - debug this bash script
#

# echo "There are around 6 mistakes"
FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1-lunch
# bug 1. SAMPLE_PREFIX variable definition missing
SAMPLE_PREFIX=SRR072
GENOME_DIR=/Users/cmdb/data/genomes
# bug 2. RESULT_DIR variable definition missing // for tophat, -o option requires a string
RESULT_DIR=dmel5
ANNOTATION=dmel-all-r5.57.gff
CORES=4

for i in {893..916}
# bug 3. do/done code missing
# bug 4/5. tophat/cufflinks inputs missing
# bug 6. echo codes were added
do
  fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR/$i
  tophat -p $CORES -G $OUTPUT_DIR/$ANNOTATION -o $RESULT_DIR$i $GENOME_DIR/dmel-all-chromosome-r5.57 $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz
  cufflinks -p $CORES -G $OUTPUT_DIR/$ANNOTATION -o $RESULT_DIR$i $RESULT_DIR$i/accepted_hits.bam
done
