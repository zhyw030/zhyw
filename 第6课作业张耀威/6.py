sum=0
def j(a,d,b,c):
    if(a==d and b==c):
        return 1
    else:
        return 0
for i in range(10000,20000):
    a=i%10    #个
    b=i//10%10      #十
    c=i//1000%10   #千
    d=i//10000%10#万
    flag=j(a,d,b,c)
    if(flag==1):
        print("%d"%i,end=(","))
        sum=sum+1






 
        
print("回文数有%d个"%sum)































