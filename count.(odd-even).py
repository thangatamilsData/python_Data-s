count=0
count1=0
for a in range(1,11):
    if(a%2==0):
        count=count+1
    elif(a%2==1):
        count1=count1+1
print(count)
print(count1)


count=0
for i in range(1,200):
    if(i%3==0 and i%5==0):
        count=count+1
        print(i)
print(count)
