def fibonacci(n):
    """
    Recursive function to generate the Fibonacci series up to n.
    """
    # base case: if n is 0 or 1, return n
    if n <= 1:
        return n

    # recursive case: return the sum of the previous two terms
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))  # take input from user

# generate and print the first n terms of the Fibonacci series using recursion
for i in range(n):
    print(fibonacci(i), end=" ")