sum=0
def j(i,c,b,a):
    if(i==c**3+b**3+a**3):
        return 1
    else:
        return 0
for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100%10
    flag=j(i,c,b,a)
    if(flag==1):
        print("%d"%i,end=(","))
        sum=sum+1






 
        
print("水仙花数有%d个"%sum)




    



"""flag=j(i,c,b,a)
if(flag==1):
    print("%d"%i,end=(","))"""
    




        
