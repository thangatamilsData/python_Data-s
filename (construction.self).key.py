class student():
    def __init__(self):
        self.name="tamil"
        self.age="22"
    def dis(self):
        print("name :",self.name)
        print("age :",self.age)

hi=student()
bye=student()

hi.name="vicky"
hi.age="22"

bye.name="sudhakar"
bye.age="22"


hi.dis()
bye.dis()
