Y=[10,20,30,40,50,60,70,80,90,100]
index=0
flag=False
num=int(input("Enter your value: "))
while index<=10 and flag==False:
    if num==Y[index]: flag=True
    else: index=index+1
if flag==True: print("Value found in ", index)
else:print("Value not found")