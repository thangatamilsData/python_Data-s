class father():
    def phone(self):
        print("yes its father's phone")

class son(father):
    def laptop(self):
        print("son's laptop")

class get(son):
    def loop(self):
        print("tamil")

h1=father()
h2=son()
h3=get()


h3.laptop()
h2.phone()
