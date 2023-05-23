'''
Python Program to find sum of digit of number using recursion.
'''

def sum_of_digits(num):

    if num < 10:
        return num

    sum1 = num % 10 + sum_of_digits(num//10)
    return sum1


num = int(input("Enter the no:"))
print(f"sum of digits {sum_of_digits(num)}")


