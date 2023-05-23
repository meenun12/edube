'''
Write a program in python to find second highest number in an array
'''

# Define an array of numbers
arr = [5, 2, 8, 3, 1, 9, 4]

# Initialize variables to hold the highest and second highest numbers
highest = arr[0]
second_highest = arr[0]

# Loop through each number in the array
for num in arr:
    # If the number is larger than the current highest, update the highest and second highest variables
    if num > highest:
        second_highest = highest
        highest = num
    # If the number is larger than the current second highest but not larger than the current highest, update the second highest variable
    elif num > second_highest and num != highest:
        second_highest = num

# Print out the second highest number
print("The second highest number is:", second_highest)




