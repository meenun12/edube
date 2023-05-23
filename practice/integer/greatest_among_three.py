'''
Write a program in Python to find greatest among three integers.
'''

a = [2, 5, 6, 12, 0, 34, 65, 2]
greatest = 2
for n in a:
    if n > greatest:
       greatest = n

print(greatest)


