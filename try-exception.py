try:
    a=int(input())
    b=int(input())
    c=a+b
    print(c)
except:
    print("invalid")

try:
    a=int(input())
    b=int(input())
    c=input()
    print(a/c)
    print(d)
except ValueError as e:
    print("value Error")
except TypeError as e:
    print("type Error")
#Exception work for all all Errors
except Exception:
    print("wrong")
finally:
    print("Done")
