'''
Given no is perfect or not
'''

def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    else:
        return False


number = int(input("Enter a number: "))
if is_perfect(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")


