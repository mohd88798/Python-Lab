# Print Fibonnacci series up to n members

n1 = 0
n2 = 1
n = 0
num = int(input("Enter a number to print fibonnaci series: "))


if num>1:
    print(n1,n2,end=' ')
    for i in range(2,num):
        n=n2+n1
        n1=n2
        n2=n
        print(n,end=' ')
elif num==1:
    print(n1)
else:
    print("Please enter a positive number")
