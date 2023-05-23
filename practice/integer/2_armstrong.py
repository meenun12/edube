'''
Write a program in Python to check whether an integer is Armstrong number or not
'''

num = 153
num_of_digits = len(str(num))

sum = 0
while num > 0:
    digit = num % 10
    sum += digit**num_of_digits
    num = num//10

if sum == num:
   print("no is armstrong number")




