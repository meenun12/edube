
'''
Python Program to Convert Decimal Number into Binary.
'''

def calculate_binary(num):

num = int(input("Enter the number:"))
binary = calculate_binary(num)

rem = []
while num >= 1:
    rem.append(num % 2)
    num = num // 2


rem = rem[::-1]
rev = ''.join(map(str, rem))
print(rev)

