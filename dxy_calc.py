import os
import pandas as pd
import numpy as np
from Bio import SeqIO
import csv
import sys

#USAGE:
#python3 dxy_calc.py alignment_directory output_file.csv
#alignment_directory contains one Scer population aligned with a Spar population, one file per gene


# dxy function for one gene
good_nucs = ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g']

def dxy(spar_seqs, scer_seqs):

    dxy = 0
    spar_strain_count, scer_strain_count = len(spar_seqs), len(scer_seqs)

    try:
        for spar_seq in spar_seqs:
            for scer_seq in scer_seqs:
                for i in range(len(spar_seq)):
                    if scer_seq[i] != spar_seq[i] and scer_seq[i] in good_nucs and spar_seq[i] in good_nucs:
                        dxy += 1

        dxy = dxy / (spar_strain_count * scer_strain_count)
        return dxy / len(spar_seqs[0])

    except:
        return 'NaN'

#filter out bad alignments
def separate_strains(file, gap_max=0.1, spar_strain_count_min=8, scer_strain_count_min=0): #.7*724

    spar_seqs, scer_seqs = [], []

    for record in SeqIO.parse(file, 'fasta'):

        if (str(record.seq).count('-') + str(record.seq).count('N') + str(record.seq).count('n')) / len(record.seq) > gap_max:

            continue

        if '_Sp_' in record.description:
            spar_seqs += [record.seq]

        elif 'ref(S288c)' not in record.description:

            scer_seqs += [record.seq]

    if len(scer_seqs) < scer_strain_count_min or len(spar_seqs) < spar_strain_count_min:

        return None, None

    return spar_seqs, scer_seqs

directory = sys.argv[1]
output = sys.argv[2]

if __name__ == '__main__':

    for file in os.listdir(directory):
        if "muscle_afa" not in file:
            continue
        gene = file.split('.')[0].split('_')[-1]

        spar_seqs, scer_seqs = separate_strains(directory+"/"+file)

        if spar_seqs and scer_seqs:

            dxy_val = dxy(spar_seqs, scer_seqs)

            with open(output, 'a') as f:
                writer = csv.writer(f)

                writer.writerow([directory, gene, dxy_val, len(spar_seqs), len(scer_seqs)])

                f.close()

            print(gene, dxy_val)
