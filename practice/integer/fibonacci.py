n = int(input("enter a number"))
prev = 0
curr = 1
print(prev, end="")
print(curr, end="")

for i in range(2, n):
    next = prev+curr
    print(next, end="")
    prev = curr
    curr = next



