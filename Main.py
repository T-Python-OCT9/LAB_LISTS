# LAB_LISTS
'''

Q1: Write a Python program to sum all the items in a list.

Q2: Write a Python program to get the largest number from a list.

Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

'''

# Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]

List1 = [2, 3, 4, 5, 15, 1, 43, 20] 

# Q1: Write a Python program to sum all the items in a list.

def Sum1():
    result : int = 0
    for i in List1 : 
        result += i 
    print("Sum of List is: " , result)

# Q2: Write a Python program to get the largest number from a list. 
   
def largest():
    largest_num = List1[0]
    for x in List1:
        if x > largest_num :
            largest_num = x
    print("Largest Number:", largest_num)

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

def odd():
    for i in range( 1200 , 2000 , 125):
         if i % 2 != 0 :
             print(i , end=' ')
    print()
 
odd_num = [i for i in range(1200 , 2000 , 125) if i%2 != 0 ]

# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_List = List1[:5]
Sum1()
largest()
odd()
print(odd_num)
print(new_List)