import random as r
a=int(input("允许的最大间隔"))
b=int(input("从多少开始"))
def yx(x,y):
    num=30
    zd=x
    ks=y
    num=num-zd-1
    print(num)
    while(num>=ks):
        a=r.randint(1,x)
        num=num-a
        print(num)
yx(a,b)






