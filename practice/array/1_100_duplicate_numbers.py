'''
Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.
'''

a = [1, 3, 4, 4, 5, 6, 6]

dup = {}
li = []
for i in a:
    if i in dup:
        li.append(i)
    else:
        dup[i] = 1

print(li)

# li = []
# for key, value in dup.items():
#     if value > 1:
#        li.append(key)
#
# print(li)



