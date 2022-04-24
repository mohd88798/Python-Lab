from logging import exception


i=["Zero","One","Two","Three"]

def index():
    ch = int(input("Enter the index of the element you want to view: "))
    try:
        print("The element is",i[ch])
    except Exception as e:
        print(e)


def zero():
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    try:
        print("Division:",a/b)
    except Exception as e:
        print(e)

# Index out of range exception if input is > 3
index()
# Division by zero exception if denominator is zero
zero()