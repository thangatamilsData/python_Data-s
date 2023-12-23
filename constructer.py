class showroom():
   
    def __init__(self):
        self.bikename=""
        self.Carname=""
    def bike(self):
        print("hi")
        print("Bike :", self.bikename)
    def car(self):
        print("Car World")

show=showroom()
room=showroom()
show.bikename="R15"

room.Carname="supra"

show.bike()

