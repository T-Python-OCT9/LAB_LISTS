list = [2, 3, 4, 5, 15, 1, 43, 20]
print(list)

x : int = 0
for i in range(len(list)):
    x = x + list[i]  
    i = i + 1 

print("the sum is: ",x)

y : int = 0
for i in range(len(list)):
    y = max(list)

print("The large number is: ",y)

new_List = list[:5]
print(new_List) 

new_List2 = [x for x in range(1200,2000,125) if x %2 != 2] 
print(new_List2)
