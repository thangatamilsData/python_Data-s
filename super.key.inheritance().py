class a():
    def __init__(self):
        print("A")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def tamil(self):
        print("tamil")

class c(b):
    def __init__(self):
        super().__init__()
        print("C")
    def hi(self):
        print("tamilan")

c1=c()


