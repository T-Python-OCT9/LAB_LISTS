
numList = [2, 3, 4, 5, 15, 1, 43, 20]

#1
SumList =sum(numList)
print("the sum od list is:",SumList)

#2
LargNum = max(numList)
print("the largest number in the list is:",LargNum)


#3

oddList = [i for i in range(1200,2000,125) if i % 2 != 0]
print("the odd list :",oddList)

#4
Slice_List = numList[:5]
print("the list after Slicing :",Slice_List)