class Shape():
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        a=10
        b=20
        print(a*b)

r1=Rectangle()

print(Shape().area())
r1.area()


class Animal():
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Bird(Animal):
    def sound(self):
        print("Birds Sing")

b1=Bird()

b1.sound()
