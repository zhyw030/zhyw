import math as m
def sss():
    if(flag==1):
        return 1
    else:
        return 0
x=0
for j in range(2,1001):
    a=j
    flag=1
    for i in range(2,a):
        if(a%i==0):
            flag=0
            break
    flag=sss()
    if(flag==1):
        print("%d"%a,end=(","))
        x=x+1
print("总共有%d个素数"%x)












