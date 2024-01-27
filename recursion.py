a = int(input("Enter the value :"))
def recursion(n):

    if n <=0 :
        return 1
    else:
        return (n* recursion(n-1))
    

if (a <= 0):
    print("Enter the larger number :")
else:
    print("the n value is ",a ,"the recursion is ", recursion(a))