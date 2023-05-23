'''
Write a program in python to find largest and smallest no in python
'''

a = [4, 1, 4, 5, 7]

smallest = a[0]
largest = a[0]

for i in a:

    if i < smallest:
        smallest = i

    if i > largest:
        largest = i

print(smallest)
print(largest)

