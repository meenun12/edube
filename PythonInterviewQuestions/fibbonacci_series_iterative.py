prev = 0
curr = 1

n = int(input("Enter a number"))

for i in range (2, n):

    next_terms = prev+curr
    print(next_terms)
    prev = curr
    curr = next_terms

