ls=[]
p=int(input("你是否要运行此程序 1.是 2.否"))
while(p!=2):
    if(p==1):
        y=int(input("请输入你要的位数"))
        for i in range(10**(y-1),10**y):
            a=str(i)
            for j in a :
                c=int(j)
                x=c**y
                ls.append(x)
            k=sum(ls)
            
            if i==k:
                print(i)
            ls=[]
    p=int(input("你是否要再次运行此程序 1.是 2.否"))
