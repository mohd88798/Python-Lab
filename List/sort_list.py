my_list=[23,99,76,34,15,49,45,13,4,8,13,8,4,8,4,4,49]

temp = 0
asc_list = []
des_list = []

def ascending():
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i]>my_list[j]:
                temp=my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=temp

def descending():
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i]<my_list[j]:
                temp=my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=temp


ch=int(input("Press \n1 to sort the list in ascending order \n2 to sort the list in descending order "))

if ch == 1:
    ascending()
    print(my_list)
elif ch == 2:
    descending()
    print(my_list)
else:
    print("Wrong input")
