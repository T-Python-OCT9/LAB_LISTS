'''
## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a Python program to sum all the items in a list.
### Q2: Write a Python program to get the largest number from a list.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''

num_list = [2, 3, 4, 5, 15, 1, 43, 20]
#the numbers list 


print(sum(num_list))
#prints out the sum of the numbers in the list


print(max(num_list))

#prints out the maximum number in the list 

odd_numbers = [x for x in range(1200,2000,125) if x % 2 != 0]
print(odd_numbers)

# odd list from range 1200-2000 using list comprehension


slice_list = num_list[:5]

print(slice_list)


    
    


