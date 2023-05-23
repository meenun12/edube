'''
Python program to perform left rotation of array elements by two positions.
'''

# Define an array of elements
arr = [1, 2, 3, 4, 5]

# Define the number of positions to rotate by
n = 2

# Perform a right rotation of the array by n positions
arr = arr[-n:] + arr[:-n]

# Print out the updated array
print(arr)
