class laptop():
    price=""
    processor=""
    Ram=""
    def HP(self):
        return "It's a great deal"
    def DELL(self):
        print("Deal of the day")
    def LENOVO(self):
        print("No offer")

lap=laptop()
top=laptop()
fix=laptop()

lap.price="50000"
lap.processor="intel core i5"
lap.Ram="8 GB"

top.price="55000"
top.processor="AMD ryzen 5"
top.Ram="16 GB"

fix.price="60000"
fix.processor="intel core i7"
fix.Ram="8 GB"

print(lap.HP())
print("price :",lap.price)
print("Processor :",lap.processor)
print("Ram :",lap.Ram)

top.DELL()
print("processor :",top.processor)
print("price :",top.price)
print("Ram :",top.Ram)
