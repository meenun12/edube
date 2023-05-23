'''
Write a program in Python to find sum of digits of a number using recursion?
'''


def sum_of_digits(n):
    """
    Recursive function to find the sum of digits of a number n.
    """
    # base case: if n is less than 10, return n
    if n < 10:
        return n

    # recursive case: return the sum of the last digit and the sum of digits of the rest of the number
    return (n % 10) + sum_of_digits(n // 10)


num = int(input("Enter a number: "))  # take input from user

# find and print the sum of digits of the number using recursion
print("The sum of digits of", num, "is", sum_of_digits(num))


