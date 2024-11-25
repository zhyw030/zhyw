sum=0
for i in range(0,101):
    a=i%10
    b=i//10%10
    c=i//100%10
    if(i%3==0 or a==3 or b==3 or c==3 ):
        sum=sum+i
print("和为%d"%sum)
         
     






























