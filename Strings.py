# In this module i am working on some basic bioinformatics concepts such as
# working on bio sequences
dna = "atgcccgcgcgatagagatatagcgacacgacgatcatc"
print(dna.count("c"))  # to find the number of specific strands in DNA

# and for the position or location we use
print(dna[-1])  # for the last position
print(dna[0])  # for the 1st position
print(dna[:3])  # upto 3 sequeces start from 0
print(dna[1:11])  # sequences between 1 to 11
print(dna[5:])  # every letter after first 5 letters
# some other functions are

# length function
print(len(dna))  # it tells the total length of the string
print(type(dna))  # to find the variable type

# Some more  useful string functions
# Such as
print(dna.upper())  # it will convert all the cases to upper case

# lets try some other functions

print(dna.replace("c", "o"))  # it will replace all "c" letters with "o"
print(dna.find("ta"))  # it starts finding the "ta" from 0th position
print(dna.rfind("ta"))  # it will find the given string form the reverse means from -1 position
