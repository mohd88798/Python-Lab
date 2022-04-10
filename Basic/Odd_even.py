# Display odd and even numbers between a given range
first = int(input("Enter first number of the range: "))
last = int(input("Enter last number of the range: "))

if(first<=last):
    print('The even numbers are: ',end='')
    for i in range(first,last+1):
        if i%2==0:
            print(i, end=' ')
    print()
    print('The odd numbers are: ',end='')
    for i in range(first,last+1):
        if i%2!=0:
            print(i,end=' ')

else:
    print('The first number of range should be smaller than the last number ')
