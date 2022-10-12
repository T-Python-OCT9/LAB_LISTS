
# Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]

num_lis :int = [2, 3, 4, 5, 15, 1, 43, 20]
#Q1Write a Python program to sum all the items in a list.
result=0
for count in num_lis:
    result += count
print(result)

#Q2 Write a Python program to get the largest number from a list.


largest=0
for x in num_lis:
    if x >largest:
        largest=x
print(largest)

#Q3 Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

odd_list=[]
for y in range(1200, 2001):
    if y % 2 != 0:
        odd_list.append(y)
print("odd numbers list from 1200 to 200 is: \n",odd_list)

#Q4  use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
print("odd numbers list fifth element to 2000 is: \n",odd_list[4:])