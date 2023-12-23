a=[]
print("Enter the natural number below")
for n in range(7):
    num=int(input("Enter the natural no :"+str(n+1)))
    a.append(num)
print(a)
print(n*n*n)

sum=0
for n in a:
    sum=sum+n
print(sum)
