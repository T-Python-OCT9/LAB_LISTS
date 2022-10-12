# this is lab4 - lists - 12oct - ghadah alharbi 
my_list= [2, 3, 4, 5, 15, 1, 43, 20]

 #Q1 : 

x=len(my_list)

n=0
list_sum=0
while n !=x:
    list_sum= list_sum + my_list[n]
    n=n+1

print (list_sum)


#Q2:
print(max(my_list)) 


#Q3:
my_list2=list()

for n in range(1200,2000,125):
    if n % 2 !=0 :
        my_list2.append(n)
 

print (my_list2)



#Q4
new_list=my_list[0:5]
print(new_list)









