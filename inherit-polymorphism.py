class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def grade(self):
        print(self.name)

s1=student("parameter")

s1.grade()
