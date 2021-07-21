class Student:
    def __init__(self):
        self.name = ""
        self.marks = 0

    def calPercentage(self):
        print((self.marks * 100) / 50)


s1 = Student()
s1.name = "ABC"
s1.marks = 35
s1.calPercentage()

s2 = Student()