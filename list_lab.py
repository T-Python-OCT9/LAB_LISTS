### Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a Python program to sum all the items in a list.
from re import I

list_1 = [2, 3, 4, 5, 15, 1, 43, 20]
sum = sum (list_1)
print (sum)
### Q2: Write a Python program to get the largest number from a list.
def largest_fun (list_1):
    print(max(list_1))

largest_Value = largest_fun(list_1)

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

All_list= [*range(1200 ,2000, 125)]
odd_list= []
for i in All_list:
    if i % 2 != 0:
        odd_list.append(i)

print (odd_list)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list= list_1[:5]
print(new_list)




