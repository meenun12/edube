
def sum_of_digits(num):

    if num <= 1:
        return num

    num = num % 10 + sum_of_digits(num//10)
    return num


num = int(input("Enter the number:"))
sum = sum_of_digits(num)
print(sum)