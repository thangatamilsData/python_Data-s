class person():
    def __init__(self,nam):
        self.name=nam

class student(person):
    def __init__(self,nam,score):
        super().__init__(nam)
        self.score=score

    def display(self):
        print(self.name,self.score)

sui=student("tamil","A")

sui.display()
