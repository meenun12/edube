'''
Python program to count Occurrence Of Vowels & Consonants in a String.
'''

input_char = input("Enter a string")

count_vowels = 0
count_con = 0

for i in input_char:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count_vowels += 1
    else:
        count_con += 1

print(f"no of vowels are {count_vowels}")
print(f"no of con are {count_con}")
