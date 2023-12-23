Tamil=int(input())
English=int(input())
Math=int(input())
Science=int(input())
Social=int(input())
Total=((Tamil+English+Math+Science+Social)/5)
if(Total>50):
    print(Total)
    print("You are good to go")
    name=input("Enter something")
    
else:
    print(Total)
    print("Additional clss is required")
