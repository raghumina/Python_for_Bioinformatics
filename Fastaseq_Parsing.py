from pandas import DataFrame
import pandas as pd

#from Bio import SeqIO
#for seq_record in SeqIO.parse("seq.fasta","fasta"):
#    print(seq_record.id)
#    print(repr(seq_record.seq))
#    print(len(seq_record))

# now converting values into ascii




data = [line.strip() for line in open("seq1.fasta", 'r')]

#print(data)
dataFrame = list([data])
print(dataFrame)


seq1 = []
count = 0
for  seq in data:
    seq1.extend(ord(num) for num in seq)
    count = count + 1
print(count, seq1)










'''
#f = open("seq1.fasta","a",encoding="utf-8")

##result = list(f.encoding(f))
#print(result)


sequence = ["ATGC"]
result
'''