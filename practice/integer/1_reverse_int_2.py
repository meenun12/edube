# Define a function to reverse an integer recursively
def reverse_num(num):

    num2 = str(num)
    num3 = num2[::-1]
    return int(num3)


# Define an integer
num = 12345

# Reverse the integer using the reverse_num() function
reversed_num = reverse_num(num)

print(reversed_num)