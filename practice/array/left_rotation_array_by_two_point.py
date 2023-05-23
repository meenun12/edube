'''
Python program to perform left rotation of array elements by two positions.
'''

a = [1, 2, 3, 4, 5, 6]

n = 2

b = a[n:] + a[:n]

print(b)
