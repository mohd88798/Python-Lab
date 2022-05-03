from SI_method import *

amount = int(input("Enter the prncipal amount: "))
rate = int(input("Enter the rate of interest(In percent): "))

print(f"The interst amount for {amount} and {rate}% rate of interest is {interest(amount,rate)}")