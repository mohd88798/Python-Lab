class AgeLowError(Exception):
    def __str__(self):
        return "Age is less than 18 you cannot drive"
class AgeHighError(Exception):
    def __str__(self):
        return "Age is greater than 65 you cannot drive"

age = int(input("Enter your age: "))

def AgeVerification(age):
    try:
        if age>18 and age<=65:
            print("You are Eligibel to drive")
        elif age<18:
            raise AgeLowError
        elif age>65:
            raise AgeHighError
    except AgeLowError as L:
        print(L)
    except AgeHighError as H:
        print(H)
        

AgeVerification(age)