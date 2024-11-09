print("=================成绩录入================")
p=1
while(p!=0):
    if(p==1):
        a=input("姓名1：")
        b=input("成绩1：")
        p=2
        num1=1
    if(p==2):
        c=input("姓名2：")
        d=input("成绩2：")
        p=3
        num2=2
    if(p==3):
        e=input("姓名3：")
        f=input("成绩3：")
        p=4
        num3=3
    if(p==4):
        g=input("姓名4：")
        h=input("成绩4：")
        num4=4
        p=0
print("本小组的成绩录入如下：")
print("序号       姓名      成绩")
print("",num1,"      ",a,"      ",b,)
print("",num2,"      ",c,"      ",d,)
print("",num3,"      ",e,"      ",f,)
print("",num4,"      ",g,"      ",h,)
if(int(b)<int(d)):
    A=d
    N=c
else:
    A=b
    N=a
if(int(f)<int(h)):
    B=h
    M=g
else:
    B=f
    M=e
if(A<B):
    C=B
    Q=M
else:
    C=A
    Q=N
print("本小组的最好成绩同学为：",Q,"     ",C,)
    
    
        
    
