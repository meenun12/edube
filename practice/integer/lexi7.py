list1 = ["apple", 5, "banana", 1, "orange", 3]
list2 = ["gobhi", 5, "onion", 2, "orange", 3]

list3 = ["oil", "pizza", 1, 2, 3]

all_present = True
for elem in list3:
    if elem not in list1 or elem not in list2:
        all_present = False
        break

if all_present:
    print("All elements in list3 are present in list1 and list2.")
else:
    print("Not all elements in list3 are present in list1 and list2.")