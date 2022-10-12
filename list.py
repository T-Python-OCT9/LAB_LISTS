
list = [2, 3, 4, 5, 15, 1, 43, 20]
sum = 0
larg = 0
for i in list:
    sum = i+sum
    if larg < i:
        larg = i

print("The sum is: " , sum)
print("The largest is: " , larg)

oddlist = []

for j in range(1200,2000,125):
    if j%2 != 0:
        oddlist.append(j)

odd = [x for x in range(1200,2000,125) if x%2 != 0 ]
print(oddlist)
print(odd)
list_slicing = list[:5]
print(list_slicing)



