from GS_method import *

net_salary = int(input("Enter the base salary: "))

print(f"The salary for permanent employee is {Salary(net_salary)}")
print(f"The salary for temporary employee is {net_salary}")