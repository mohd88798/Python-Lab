class Distance:
    def __init__(self):
        self.d1_feet = 0
        self.d1_inch = 0
        self.d2_feet = 0
        self.d2_inch = 0

    def getData(self):
        print("Enter 1st Distance: ")
        self.d1_feet = int(input("Enter feet: "))
        self.d1_inch = int(input("Enter inch: "))
        print("\nEnter 2nd Distance: ")
        self.d2_feet = int(input("Enter feet: "))
        self.d2_inch = int(input("Enter inch: "))

    def add(self):
        result_feet = self.d1_feet + self.d2_feet
        result_inch = self.d2_inch + self.d1_inch

        while result_inch >=12:
            result_inch-=12
            result_feet+=1

        print(f"\nSum of distance is {result_feet} feet and {result_inch} inch")

d = Distance()
d.getData()
d.add()
        