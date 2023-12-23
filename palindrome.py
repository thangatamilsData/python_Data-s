while True:
    a = input("Enter the value :")

    rev = a[:: -1]

    if a == rev :
        print("palindrome")
        break
    else:
        print("it's not")
