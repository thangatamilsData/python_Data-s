class center():
    def __init__(self,t,a,w):
       self.name=t 
       self.age=a
       self.work=w
class right(center): #inheritance
    def display(self):
        print(self.name,self.age,self.work)
class left(right): #polymorphism - overRide
    def display(self):
        print("hi iam tamil")

hi=left("tamil","22","IT")


hi.display()


#encapsulation
class shop():
    def __init__(self,m1):
        self.__wear=m1
    def shirt(self):
        print(self.__wear)
        
so=shop("nice T-shirt")

so.shirt()

print(so.__wear()) #can't get because of object is in priviate
