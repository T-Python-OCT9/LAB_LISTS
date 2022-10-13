# LABLISTS

## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
new_list = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a Python program to sum all the items in a list.
sum =0
for i in new_list:
    sum += i
print("sum all the items: " , sum )

### Q2: Write a Python program to get the largest number from a list.
 #first 
'''
new_list.sort()
print("Largest element is:", new_list[-1]) 
'''

larg = new_list[0]
small =0
for a in new_list:
    if a > larg:
       
        larg = a
print("largest number : " , larg )
     
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

odd_num = list() 
for num1 in range(1200 , 2000 , 125 ):
    
    if num1 %2==0:

     odd_num.append(num1)

print( "odd numbers list " ,odd_num)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_list2 = new_list[:4]
print( " 5th element in the list :" , new_list2)