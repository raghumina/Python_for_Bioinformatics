# a fasta file
# FASTA format file




# >AC073210.8 Homo sapiens BAC clone RP11-460N20 from 7, complete sequence
f = open("Sequence.txt","r")
print(f)
for words in f:
    if words == "C":
        print(words)