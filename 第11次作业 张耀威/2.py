c=[]
def sl(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return sl(n-1)+sl(n-2)
def qz(n):
    for i in range(1,n+1):
        c.append(sl(i))
    print(c)
    a=0
    for i in range(n):
        a=a+c[i]
    print(a)
qz(20)
"""for i in range(n-1,1,-1):
        a=c[n-1]+c[n-2]
        del c[n-1]
        del c[n-2]
        c.append(a)
    print(a)

qz(10)
print(c)
a=0
for i in range(3):
    a=a+c[i]
for i in range(10,3,-1):
    print(i)"""
    



