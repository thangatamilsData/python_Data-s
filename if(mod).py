a=int(input("Enter the Value"))
if(a%2==0):
    print("Even")
else:
    print("Odd")

score=int(input("Enter the Marks"))
if(score>35):
    print("Good",score,"/100")
else:
    print("Have to Improve",score,"/100")


score=int(input("Enter the Score"))
if(score<35):
    print("Have to improve Much")
if(score>35 and score<70):
    print("Good not enough")
else:
    print("Very Good")



score=int(input("Enter the Score"))
if(score<35):
    print("Have to improve Much")
elif(score>35 and score<70):
    print("Good not enough")
else:
    print("Very Good")
