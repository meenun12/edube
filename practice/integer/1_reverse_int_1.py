# Define a function to reverse an integer recursively
def reverse_num(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10) + str(reverse_num(num // 10)))

# Define an integer
num = 12345

# Reverse the integer using the reverse_num() function
reversed_num = reverse_num(num)

aprint(reversed_num)