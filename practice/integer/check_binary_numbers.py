'''
Write a program in python to check if number is binary
'''

a = input("Enter a binary number")

for i in a:
    if i not in ["0", "1"]:
        print("Number is not a binary number")
        break
    else:
        print("Number is not a binary number")