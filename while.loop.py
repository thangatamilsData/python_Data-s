a=[1,2,3,4,5]
print(a[0])

b=[1,2,3,4,5]
b.insert(1,22)
print(b)

c=[1,2,3,4,5,6]
c[2]=20
print(c)


d=[1,2,3,4,5]
d.pop(2)
print(d)


g=[1,2,3]
h=[55,66]
g.extend(h)
print(g)

#while loop Run until it become false 
i=10
while(i<100):
    print(i,end=",")
    i=i+10
