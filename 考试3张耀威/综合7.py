sum=0
for j in range(1000,2001):
    a=j
    flag=1
    for i in range(2,a):
        if(a%i==0 or (a+2)%i==0):
            flag=0
          
    if(flag==1):
        print("(%d,%d)是孪生素数"%(j,(j+2)))
        sum=sum+1
print("总共有%d个孪生素数"%sum)
