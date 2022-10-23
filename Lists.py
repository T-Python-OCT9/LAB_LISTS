


Abdulelah_list = [2, 3, 4, 5, 15, 1, 43 20 ]

print(mAbdulelah_list)

sum_result: int = 0
largest_number: int = 0
for i in Abdulelah_list:
    sum_result += i

print(sum_result)


for i in Abdulelah_list:
    if i > largest_number:
        largest_number = i

print(largest_number)

odd_numbers = [i for i in range(1200, 2000, 125) if not i % 2 == 0]
print(odd_numbers)

new_list = Abdulelah_list[:4]

print(new_list)


'''
Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a Python program to sum all the items in a list.
Q2: Write a Python program to get the largest number from a list.
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''
