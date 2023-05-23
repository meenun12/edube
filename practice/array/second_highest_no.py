l = [3,4,2,1]

highest = l[0]
second_highest = l[0]

for i in l:

    if i > highest:
        second_highest = highest
        highest = i
    elif i > second_highest and i != highest:
        second_highest = i




