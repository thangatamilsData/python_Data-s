#fibonacci
def fibo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c)

fi = fibo(20)

#factorial

a = int(input("Enter the number"))

fact = 1

for i in range (1,a+1):
    fact = fact*i
print(fact)
