list = [2, 3, 4, 5, 15, 1, 43, 20]

# Q1: Write a Python program to sum all the items in a list.

sum = 0

for i in list:
    sum = sum + i

print(sum)

# Q2: Write a Python program to get the largest number from a list.

largest = 0

for i in list:
    if i > largest:

        largest = i
    
print(largest)



# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

odd = [i for i in range(1200, 2000, 125) if not i % 2 == 0]
print(odd)

# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

s_list = list[0:4]

print(s_list)


    




