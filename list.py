number_list = [2, 3, 4, 5, 15, 1, 43, 20]
print("the sum list =", sum(number_list))

largest = number_list[0]
for i in number_list:
    if i > largest:
        largest = i

print("the largest number of list =",largest)



newlist = [x for x in range(1200, 2000, 125) if x%2 != 0 ]

print(newlist)

new_list = number_list[:5]
print(new_list)

