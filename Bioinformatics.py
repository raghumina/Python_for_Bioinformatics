# In this module i am working on some basic bioinformatics concepts such as
# working on bio sequences
'''
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

# Some more useful String functions

print(dna.islower())  # boolean conditions checks the condition and return True or False
print(dna.isupper())  # checks for upper case words
print(dna.isspace())  # checks for space
print(dna.isnumeric())  # Checks weather the variable is numeric or not

# lets practice a simple program

# read DNA sequence for user and count the number of "c" in it.
# also determine the length of the DNA

dna1 = input("Please enter your sequence here\n")
dna_str = str(dna1)
print("The count of c in DNA is:", dna1.count("c"), "\nThe length of DNA is:", len(dna1))

print(int(4+6/2+2*2))
#print('dna'+1+2+3)

dna="atgctggggact"
print(dna[:3])


seqlen = '10bp'
seqlen='2'+seqlen
seqlen=seqlen*2
print(seqlen)
'''

# List in Python

gene_expression = ["gene", 5.15e-08, 0.000381, 7.33e-08]
print(gene_expression)

# Assigning a new value to the variable
gene_expression[0] = "Dna"
print(gene_expression)  # this will add the Dna on the 0th position on the variable

# list as Stack
stack = ["12", "2", "3", "4"]  # Stack uses the concept of LIFO    last in first out
print(stack)
stack.append("99")  # will add the given value in the last of the list
print(stack)
# lets try some other example
# append a list in a list
stack.append(["100", "101", "102", "103"])
print(stack)  # it will make the list a value in the list did not add the list

# lets try extend
stack.extend(["11", "22", "33", "444", "555"])
print(stack)  # yes extend adds a list in a list

# lets use pop function
element = stack.pop()  # removes the last value from the list
print(element)  # this will show the popped value
print(stack)  # show the complete list after pop

stack1 = [11, 23, 45, 54, 65, 22]
print(sorted(stack1))  # it will sort the list in a order

# Tuples

# for example
t = 1, 2, 3, 4, 5, 6, 7, 8
print(t)

