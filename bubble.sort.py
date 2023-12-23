#bubble sort 
def sort (nums) :
    for i in range(len (nums)-1,0,-1) :
        for j in range(i) :
            if nums[j]>nums [j+1]:
                temp = nums [j]
                nums [j] = nums[j+1]
                nums [j+1] = temp

                
nums = [5, 3, 8, 6, 7, 2]
sort (nums)

print (nums)

#Greatest three number
a = 10
b = 20
c = 30
count = 0
while True:
    count +=1
    x = int(input("Enter the number :"))
    if a >= x:
        print("its wrong")
        

    elif b >= x:
        print("its wrong")
        
    elif c >= x:
        print("crt !")
        break
        
print(count)
    
