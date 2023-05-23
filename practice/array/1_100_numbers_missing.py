'''
Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.
'''

a = [3,6,7,8,1,2,4,10,11,12,15,9]
b = sorted(a)
start = 1
missing = []
for i in b:
    if start not in b:
        missing.append(start)
    start += 1

print(missing)

