the_list = [2, 3, 4, 5, 15, 1, 43, 20]

# Q1: Write a Python program to sum all the items in a list.
sum : int = 0
for item in the_list:
    sum = sum + item
print(sum)

# Q2: Write a Python program to get the largest number from a list.
largest = the_list[0]
list_len = len(the_list)
for item in the_list:
    if largest < item:
        largest = item
print(largest)

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
odd_list = [number for number in range(1200, 2000, 125) if number % 2 != 0]
print(odd_list)

# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list = the_list[:5]
print(new_list)