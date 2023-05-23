'''
Write a program in python to find top two max value in an array
'''

a = [1, 3, 100, 5]
highest = a[0]
second_highest = a[0]

for i in a:

    if i > highest:

       second_highest = highest
       highest = i

    elif i > second_highest and i != highest:

        second_highest = i


print(f"highest:{highest}")
print(f"second highest:{second_highest}")


