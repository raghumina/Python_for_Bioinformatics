#

from Bio import SeqIO

from Bio import SeqIO

for r in SeqIO.parse("seq1.fasta", "fasta"):
    r.letter_annotations["solexa_quality"] = [12] * len(r)
    print(r.format("fastq"),end="")





print(r)
def QtoPhred33(Q):
    return chr(Q + 33)
Q = r.format("fastaq")
print(QtoPhred33(Q))