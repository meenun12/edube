num = int(input("Enter an integer: "))  # take input from user
reverse_num = 0  # initialize the reverse number variable to 0

while num > 0:
    # get the last digit of the number and add it to the reverse number
    last_digit = num % 10
    reverse_num = (reverse_num * 10) + last_digit
    
    # remove the last digit from the original number
    num = num // 10

print("The reverse of", num, "is", reverse_num)