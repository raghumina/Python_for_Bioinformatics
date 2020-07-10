# Sequence Strings
# bio Sequences
# import random
#

'''
seq1 = 'ATGC'
seq2 = 'GCAT'
print(seq1 + seq2)
seq3 = seq1 + seq2

seq = ['A', 'T', 'G', 'C', 'T', 'G', ]
print(''.join(seq))

import random

random.choice("ACGT")
print(random.choice("ACGT"))

# A fixed output in the random function
print(random.seed(7))

# for long random sequence
#

seq12 = ''
for _ in range(100):
    seq12 += random.choice("ATGC")

print(seq12.lower())


def longest(s1, s2):
    i = 0
    while i <= len(s1) and i <= len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]


print(longest('ATACGTGCT', 'ATAACACVAC'))
'''

# function to check the exact similarity of the strings

def match(s1, s2):
    while s1 == s2 and s2 == s1:
        return print(s1 , s2 ,"are similar")
    else:
        print("NOT SIMILAR")


print(match('ATCCTE','ATCCT'))

# the another way to check is
#
def match1(s1, s2):
    if not len(s1) == len(s2):
        return False
    
