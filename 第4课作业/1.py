def BIM():
    p=1
    while(p!=0):
        w=float(input("请输入你的体重(KG):"))
        h=float(input("请输入你的身高(m):"))
        bim=w/(h*h)
        print("BIM为%.2f"%bim)
        p=input("你是否要再来一次 1.是 2.否")
        if(p=="1"):
            p=1
        else:
            p=0
BIM()
