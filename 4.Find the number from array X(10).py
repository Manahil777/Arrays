X=[10,20,30,40,50,60,70,80,90,100]
Flag=False
num=int(input("Enter a number to search: "))

for i in range(10):
    if num==X[i]:
        Flag=True
        break
if Flag==True: print("value is found at index",i)
if Flag==False:print("value is not found")