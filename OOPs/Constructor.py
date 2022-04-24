class Students:
    def __init__(self):
        self.name=""
        self.branch=""

    def getData(self):
        self.name=input("Enter your name: ")
        self.branch=input("Enter your branch: ")

    def __str__(self):
        return f"The name of the students is {self.name} and the branch is {self.branch}"


    # def display(self):
    #     print("--------------------")
    #     print("Name:  ",self.name)
    #     print("Branch:",self.branch)
    #     print("--------------------")


stu = int(input("Enter number of student data you want to insert: "))


l = []
for i in range(1,stu+1):
    s = Students()
    print(f"Student[{i}]:")
    s.getData()
    l.append(s)
    

for i in range(stu):
    print()
    # l[i].display()
    print(l[i])