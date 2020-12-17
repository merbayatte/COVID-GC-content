#!/usr/bin/env python3
import os
import csv
from Bio import SeqIO
from Bio.SeqUtils import GC
#folder = '/bigdata/gen220/mlope072/COVID19FASTA'
outfile = "samples_GC.tsv"
folder = 'data' # I moved the data local to the github since it isn't big
files = { 'SampleL':  'EPI_ISL_685261.fasta',
          'SampleS':  'EPI_ISL_702206.fasta',
          'SampleV':  'EPI_ISL_700389.fasta',
          'SampleG':  'EPI_ISL_700740.fasta',
          'SampleGH': 'EPI_ISL_700544.fasta',
          'SampleGR': 'EPI_ISL_700322.fasta',
          'SampleGV': 'EPI_ISL_706965.fasta'}

GC_info = []
for sample in files:
    filepath = os.path.join(folder,files[sample])
    record = SeqIO.read(filepath, "fasta")
    GCcount = GC(record.seq)
    print("GC of {} ({}) is {}".format(sample,filepath,GCcount))
    GC_info.append([sample,GCcount])

# write same data to a TSV file

with open(outfile,"wt") as fh:
    outtsv = csv.writer(fh,delimiter="\t")
    outtsv.writerow(["Sample","GC"])
    for GCrow in GC_info:
        outtsv.writerow(GCrow)
