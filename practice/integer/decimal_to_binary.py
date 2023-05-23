'''
Python Program to Convert Decimal Number into Binary.
'''

num = int(input("Enter the number:"))

rem = []
while num >= 1:
    rem.append(num % 2)
    num = num // 2


rem = rem[::-1]
rev = ''.join(map(str, rem))
print(rev)

