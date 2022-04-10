# Print an n digit number in reverse order

number = int(input('Enter a number: '))
result = 0
lastdigit = 0
while number!=0:
    lastdigit = number%10
    number = number//10
    result = result*10 + lastdigit

print(f"The reverse of the given number is {result}")