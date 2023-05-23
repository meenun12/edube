'''
Python program to check given character is digit or not.
'''

def check_digit(char):
    """
    This function checks whether a given character is a digit or not.
    """
    if char.isdigit():
        print(char, "is a digit.")
    else:
        print(char, "is not a digit.")

# Example usage
check_digit('5')
check_digit('a')
check_digit('0')
check_digit('$')






