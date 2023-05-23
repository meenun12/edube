'''
Python program to count alphabets, digits and special characters.
'''

a = "This is a frog?"

digit = 0
alpha = 0
special = 0
for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1
    else:
        special += 1

print(f"digit={digit}alpha={alpha}special={special}")



