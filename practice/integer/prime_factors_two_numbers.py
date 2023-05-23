'''
Write a program in Python to find prime factors of a given integer?

'''

def prime_factors(n):
    """
    Function to find the prime factors of a given integer n.
    """
    factors = []  # list to store the prime factors

    # divide the number by 2 as many times as possible
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # check odd numbers up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # if n is still greater than 2, it must be a prime number
    if n > 2:
        factors.append(n)

    return factors


num = int(input("Enter a number: "))  # take input from user

# find and print the prime factors of the number
print("The prime factors of", num, "are:", prime_factors(num))



