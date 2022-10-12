

#List for Q1 and Q2

numberList=[2, 3, 4, 5, 15, 1, 43, 20]

#_______________________________________________


#Q1
def SumNumber():
    number=0
    for element in numberList:
        number=number+element
        
    return number


print(SumNumber())



#_______________________________________________

#Q2



print("Largest number is:", max(numberList))


#_______________________________________________

#Q3






oddNumber = [x for x in range(1200,2000,125) if x%2 !=0]
print(oddNumber)




#Q4

newlist2=numberList[:5]

print(newlist2)








