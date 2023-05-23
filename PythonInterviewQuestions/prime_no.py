'''
Write a program in Python to check given number is prime or not.
'''

num = int(input("Enter a number: "))  # take input from user

# check if the number is divisible by any number other than 1 and itself
for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")



