'''
Python program to check given character is vowel or consonant
'''

vowels = ['a', 'e', 'i', 'o', 'u']

input_chr = 'j'

if input_chr.isalpha():
    if input_chr in vowels:
        print("given character is vowels")
    else:
        print("given character is consonant")





