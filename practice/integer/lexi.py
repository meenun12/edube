list1 = ['b', 'a', 'c', 2, 1, 3]
list2 = [5, 'd', 'e', 'f', 4, 'g']
test_list = ['a', 4, 'g', 'b', 6, 'd']

list1.sort()
list2.sort()

for elem in test_list:
    if isinstance(elem, str):
        if elem in list1 or elem in list2:
            print(f"{elem} is in either list 1 or list 2.")
        else:
            print(f"{elem} is not in either list 1 or list 2.")
    elif isinstance(elem, int):
        if elem in list1 or elem in list2:
            print(f"{elem} is in either list 1 or list 2.")
        else:
        else:
            print(f"{elem} is not in either list 1 or list 2.")
