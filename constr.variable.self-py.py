class cloth():
    def __init__(self,t,m,l):
        self.shirt=t
        self.pant=m
        self.Tshirt=l
    def declar(self):
        print("Categories :",self.shirt,self.pant,self.Tshirt)

shop=cloth("adiddas","nike","vegas")

shop.declar()
