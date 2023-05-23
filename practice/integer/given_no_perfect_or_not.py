'''
Write a program in Python to find given number is perfect or not?
A perfect number is a positive integer that is equal to the sum of its proper divisors.
'''

def is_perfect(num):

    a = []
    for i in range (1, num):
        if num % i == 0:
           a.append(i)

    if num == sum(a):
        return True
    else:
        return False


num = int(input("Enter the number:"))
if is_perfect(num):
    print("Number is perfect")
else:
    print("Number is not perfect")



