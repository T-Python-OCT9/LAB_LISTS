List = [2, 3, 4, 5, 15, 1, 43, 20]

#first solution
#print(sum(List))
#print(max(List))

#odd_num=[i for i in range (1200 ,2000,125)if i%2 !=0]
#print(odd_num)


 #الحل الاصح   


def sum1():
    result : int = 0
    for i in List:
        result += i
    return result

def Largest():
    largest = List[0]
    for i in List:
        if i > largest :
            largest = i
    return largest


def odd():
    for i in range(1200 , 2000 , 125):
        if i%2 !=0 :
           print(i)
        print()

new_list = list[:5]
print(new_list)
print(sum1())
print(Largest())
odd()    

