#To sum the list and print the result 
Num_list =[2, 3, 4, 5, 15, 1, 43, 20]
list_Sum = sum(Num_list)
print("The total sum of list is : ",list_Sum)
#To find the largest number of the list and print the result
list_Max = max(Num_list)
print("The largest number of list is : ", list_Max)
# to print the odd number in the list and skip 125
for i in range(1200, 2000, 125) :
    if i % 2 == 1:
        print ('This will print only odd numbers:', i)
# to slicing the list from the first element to the 5th element
slicing_list = Num_list[0:5]
print("After slicing the list : ",slicing_list)    