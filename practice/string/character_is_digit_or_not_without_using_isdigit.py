'''
This function checks whether a given character is a digit or not.
'''

def check_digit(char):
    """
    This function checks whether a given character is a digit or not.
    """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if char in digits:
        print(char, "is a digit.")
    else:
        print(char, "is not a digit.")

# Example usage
check_digit('5')
check_digit('a')
check_digit('0')
check_digit('$')







