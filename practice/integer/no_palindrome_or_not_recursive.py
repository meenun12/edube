# Define a function to check whether a number is palindrome or not recursively
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)

    # Base case: if the string has length 0 or 1, it is a palindrome
    if len(num_str) <= 1:
        return True

    # Recursive case: check the first and last characters of the string
    # If they are the same, call the function recursively with the middle part of the string
    # Otherwise, the number is not a palindrome
    if num_str[0] == num_str[-1]:
        return is_palindrome(num_str[1:-1])
    else:
        return False

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check whether the number is palindrome or not using recursion
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
