Y=[0.1,0.0,9.9,100.9,80.0]
flag=False
num=float(input("Enter a value to search: "))

for i in range(5):
    if num==Y[i]:
        Flag=True
        break
if Flag==True: print("value found at index",i)
if Flag==False: print("value not found")