list1 = [2, 3, 4, 5, 15, 1, 43, 20]
# Q1: Write a Python program to sum all the items in a list.
sum_list = sum(list1)
print("sum:", sum_list)
# Q2: Write a Python program to get the largest number from a list.
print("the largest number from a list:", max(list1))
# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
odd_list = []
for i in range(1200, 2000, 125):
    if (i % 2 != 0):
        odd_list.append(i)


print(odd_list)


# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list = list1[5:]
print(new_list)
