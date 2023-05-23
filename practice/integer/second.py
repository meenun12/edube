"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

def df(A):

    A = [a for a in A if a > 0]

    if len(A) == 0:
       return 1

    A.sort()

    smallest = 1

    for a in A:
        if smallest == a:
           smallest = smallest+1
        if a > smallest:
            return smallest


next = df([1,1,2,3,4,5,6])
print(next)











