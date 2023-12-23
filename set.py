car={
    'toyato' : 'supra',
    'bmw' : 'mv4',
    'honda' : 'civic',
    }
car.update({'bens' : 'none'})


print(car['bens'])


for key, value in car.items():
    print(key, value)
