def solution(A):
    # Remove all negative numbers and 0 from the list
    A = [a for a in A if a > 0]

    # If there are no positive numbers, return 1
    if len(A) == 0:
        return 1

    # Sort the list
    A.sort()

    # Find the smallest missing positive integer
    smallest = 1
    for a in A:
        if a == smallest:
            smallest += 1
        elif a > smallest:
            return smallest

    # If all positive integers are present, return the next one
    return smallest


solv = solution([1,2,1,6])
print(solv)