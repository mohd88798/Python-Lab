class Box:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

class Cuboid(Box):
    def __init__(self,length,width,height):
        super().__init__(length,width,height)

    def area(self):
        return "Area of rect = ",(self.width*self.length + self.width*self.height + self.length*self.height)

class Color(Cuboid):
    def __init__(self,length,width,height,color):
        super().__init__(length,width,height)
        self.color = color

    def area(self):
        a = 2*(self.width*self.length + self.width*self.height + self.length*self.height)
        return f"Area of cuboid is {a} and color is {self.color}"
    

length = int(input("Enter the length of cuboid: "))
width = int(input("Enter the width of cuboid: "))
height = int(input("Enter the height of cuboid: "))
color = input("Enter the color of cuboid: ")

rec = Color(length,width,height,color)

print(rec.area())