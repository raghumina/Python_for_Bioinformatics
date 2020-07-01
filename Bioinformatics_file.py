# a fasta file
# FASTA format file




# >AC073210.8 Homo sapiens BAC clone RP11-460N20 from 7, complete sequence

X_File = open('Sequence.txt')
for word in X_File:
    print(X_File.read())

x_file = open('Sequence.txt','w')
x_file.write("the sequecne are\n")
print(x_file)
