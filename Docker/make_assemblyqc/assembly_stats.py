#!/usr/bin/python

"""
This script calculates all the basic length metrics for the given input genome assembly.

Usage: python3/Python-3.6.4/python assembly_stats.py <genome assembly file (fasta format)> <output file name> <estimated genome size (in Mb)> 

"""

from Bio import SeqIO
import sys
import statistics
import numpy as np



inputfile = sys.argv[1]
outputfile = sys.argv[2]
estimated_genome_size = float(sys.argv[3])

sys.stdout=open(outputfile,"w")

records = list(SeqIO.parse(inputfile, "fasta"))

number_of_scaffolds = len(records)

print("Number of scaffolds:", number_of_scaffolds)



len_seq = [len(rec) for rec in records]

total_size_scaffolds = sum(len_seq)

print("Total size of the scaffolds:", total_size_scaffolds)

total_scaffold_length_percentage_genome_size = ((total_size_scaffolds/(estimated_genome_size*1000000))*100)

print("Total scaffold size as percentage of assumed genome size:", total_scaffold_length_percentage_genome_size)

number_seq_greater_25k = sorted(i for i in len_seq if i>25000)

print("Useful amount of scaffold sequences (>=25 Kb):", sum(number_seq_greater_25k))

print("% of estimated genome that is useful:", (sum(number_seq_greater_25k)/(estimated_genome_size*1000000))*100)

print("Longest scaffold (bp):", max(len_seq))

print("Shortest scaffold (bp):", min(len_seq))

number_seq_greater_1k = len(sorted(i for i in len_seq if i>1000))

print("Number of scaffolds > 1 Kb:", number_seq_greater_1k)

print("Percentage of scaffolds > 1 Kb:", (number_seq_greater_1k/number_of_scaffolds)*100)

number_seq_greater_10k = len(sorted(i for i in len_seq if i>10000))

print("Number of scaffolds greater than 10 Kb:", number_seq_greater_10k)

print("Percentage of scaffolds greater than 10 Kb:", (number_seq_greater_10k/number_of_scaffolds)*100)

number_seq_greater_100k = len(sorted(i for i in len_seq if i>100000))

print("Number of scaffolds greater than 100 Kb:", number_seq_greater_100k)

print("Percentage of scaffolds greater than 100 Kb:", (number_seq_greater_100k/number_of_scaffolds)*100)

number_seq_greater_1M = len(sorted(i for i in len_seq if i>1000000))

print("Number of scaffolds greater than 1 Mb:", number_seq_greater_1M)

print("Percentage of scaffolds greater than 1 Mb:", (number_seq_greater_1M/number_of_scaffolds)*100)

number_seq_greater_10M = len(sorted(i for i in len_seq if i>10000000))

print("Number of scaffolds greater than 10 Mb:", number_seq_greater_10M)

print("Percentage of scaffolds greater than 10 Mb:", (number_seq_greater_10M/number_of_scaffolds)*100)


#calculates N50 and L50 values
sorted_len = sorted(len_seq, reverse=True)

sum_sorted_length = sum(sorted_len)

testSum = 0

N50 = 0

N50con = 0

L50 = 0

i = 0

for con in sorted_len:

    testSum += con

    N50con += 1

    i += 1

    if sum_sorted_length/2.0 < testSum:

       N50 = con

       L50 = i

       break



print ("N50 (bp):", N50)

print ("L50:", L50)


#calculates NG50 and LG50 values
testSumNG50 = 0

NG50 = 0

NG50con = 0

LG50 = 0

j = 0



for conNG50 in sorted_len:

    testSumNG50 += conNG50

    NG50con += 1

    j += 1

    if (estimated_genome_size*1000000)/2.0 < testSumNG50:

       NG50 = conNG50

       LG50 = j

       break



print ("NG50:", NG50)
print ("LG50:", LG50)

#calculates A,C,G,T,N percentages
counterA1 = 0
counterA2 = 0

for record in records:

    counterA1 += record.seq.count('A') 
    counterA2 += record.seq.count('a')


print ("%A:", ((counterA1+counterA2)/total_size_scaffolds)*100)


counterC1 = 0
counterC2 = 0

for record in records:
    
    
    counterC1 += record.seq.count('C')
    counterC2 += record.seq.count('c')


print ("%C:",((counterC1+counterC2)/total_size_scaffolds)*100)

counterG1 = 0
counterG2 = 0

for record in records:

    counterG1 += record.seq.count('G')
    counterG1 += record.seq.count('g')

print ("%G:",((counterG1+counterG2)/total_size_scaffolds)*100)



counterT1 = 0
counterT2 = 0

for record in records:

    counterT1 += record.seq.count('T')
    counterT2 += record.seq.count('t')

print ("%T:",((counterT1+counterT2)/total_size_scaffolds)*100)



counterN = 0

for record in records:

    counterN += record.seq.count('N')


print ("Number of Ns:", counterN)
print ("%N:", (counterN/total_size_scaffolds)*100)

sys.stdout.close()
