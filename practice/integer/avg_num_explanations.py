'''
Python Program to find the Average of numbers with explanations.
'''

def calculate_average(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return None

    # Calculate the sum of the numbers in the list
    total = sum(numbers)

    # Calculate the average by dividing the sum by the number of elements
    average = total / len(numbers)

    # Return the average
    return average


# Define a list of numbers to test the function
numbers = [1, 2, 3, 4, 5]

# Call the function and print the result
result = calculate_average(numbers)
print("The average of", numbers, "is", result)