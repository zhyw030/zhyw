import math as m

x=0
for j in range(2,1001):
    a=j
    flag=1
    for i in range(2,a):
        if(a%i==0):
            flag=0
            break
    
    if(flag==1):
        print("%d是素数"%a,end=(","))
        x=x+1
print("总共有%d个素数"%x)
