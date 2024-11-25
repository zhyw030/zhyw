d={}
ls=[]
p=0
p=input("请输入你要用的模式 1.录入商品 2.查询商品 3.退出")
while(p!=3):
    if(p=="1"):
        name=input("请输入要创建的文件名称:")
        f=open(name,"a")
        bh=input("请输入商品编号:")
        while(bh!=""):
            f.write(bh)
            f.write(",")
            goods1=input("请输入商品名称:")
            f.write(goods1)
            f.write(",")
            ls.append(goods1)
            goods2=input("请输入商品价格:")
            f.write(goods2)
            f.write(",")
            ls.append(goods2)
            goods3=input("请输入商品数量:")
            f.write(goods3)
            f.write(",\n")
            ls.append(goods3)
            d.update({bh:ls})
            ls=[]
            bh=input("请输入商品编号:")
        f.close()
        p=input("请输入你要用的模式 1.录入商品 2.查询商品 3.退出")
    elif(p=="2"):
        
        num=input("请输入编码")
        if(num!=""):
            v=d[num]
            print("商品名称：{},商品价格：{},商品数量：{}".format(v[0],v[1],v[2]))
            num=input("请输入编码")

