my_list=[23,15,49,45,13,4,8,13,8,4,8,4,4,49]
count=0
occur=[]
num = int(input("Enter a number to search: "))
for i in range(len(my_list)):
    if my_list[i]==num:
        count+=1
        occur.append(i)

print(f"The number {num} occured {count} times and the index of each occurrence are {occur}")
