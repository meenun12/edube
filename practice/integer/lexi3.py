list1 = ['a', 'b', 'c', 1, 2]
list2 = ['r', 1, 'g', 'h', 2]
list3 = [0, 'a', 2, 'c']

def fun (list1, list2, list3):

    list1 = set(list1)
    list2 = set(list2)
    list3 = set(list3)

    if list3.issubset(list1.union(list2)):

       for i, val in enumerate(list3):
           if val.isdigit():
               if any(x.isalpha() for x in list3[i+1:]):
                   return False
               break
           return False
    else:
       return False









