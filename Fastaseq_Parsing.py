
#
from Bio import SeqIO
for seq_record in SeqIO.parse("seq.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


# now converting values into ascii
#data = [line.strip() for line in open("seq1.fasta", 'r')]
#a = data.count("A")
#print(a)

#seq1 = []
#for  seq in data:
#    seq1.extend(ord(num) for num in seq)
#print(" %s"%(seq1))

