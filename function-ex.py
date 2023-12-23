a=int(input("Enter the number"))
def findevenorodd(a):
    if(a%2==0):
        print("Even")
    else:
        print("odd")
        
findevenorodd(a)

b=int(input("Enter the number"))
def findpassorfail(c):
    if(b>35):
        print("pass")
    else:
        print("fail")

findpassorfail(b)


username="tamil"
password="12345"

uname=input("Enter the name")
pword=input("Enter the password")

def value():
    if (username==uname and password==pword):
        return True
    else:
        return False


print(value())
