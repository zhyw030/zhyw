d={}
rx={}
jg=[]
ls=[]
name=input("请输入要创建的文件名称:")
f=open(name,"a")
c=open("热销产品","w")
xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")
while(xz!=7):
#----------------------增加-----------#
    if(xz=="1"):
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
            sl=int(goods3)
            f.write(goods3)
            f.write(",\n")
            ls.append(goods3)
            d.update({bh:ls})
            rx.update({sl:goods1})
            jg.append(sl)
            ls=[]    
            bh=input("请输入商品编号:")
        f.close()
        xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")

        

#——-------------删除----------------
    if(xz=="2"):
        m=input("请输入你要删除商品的编码")
        while(m!=""):
            hw=d.pop(m,"不存在此商品")
            if(hw!="不存在此商品"):
                print("以删除{}".format(hw[0]))
            else:
                print(hw)
            m=input("请输入你要删除商品的编码")
        xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")

#------------------查询---------------
    if(xz=="3"):
        cx=input("请输入你要查询的商品编码")
        while(cx!=""):
            pi=d.pop(cx,"不存在此商品")
            if(pi!="不存在此商品"):
                print("该编码对应的商品为{}，价格为{}，商品数量为{}".format(pi[0],pi[1],pi[2]))
                d.update({cx:pi})
            else:
                print(pi)
            cx=input("请输入你要查询的商品编码")
        xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")

#------------------收银------------------
    if(xz=="6"):
        cod=input('请出示付款码！')
        while(cod!=""):
            if len(cod)!=18 or (cod[0:2] not in {'10','11','12','13','14','15'}):
                print("不是有效付款码")
                cod=input('请出示付款码！')

            else:
                print("已收银")
                cod=input('请出示付款码！')

        xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")

#------------------统计——————————
    if(xz=="5"):
        for j in range(len(jg)-1):
            for i in range(len(jg)-j-1):
                if(jg[j]<jg[j+i+1]):
                    jg[j],jg[j+i+1]=jg[j+i+1],jg[j]
        for j in range(3):
            x=jg[j-1]
            sp=rx[x]
            c.write("销售第{}名是{}\n".format((j+1),sp))
            print("销售第{}名是{}".format((j+1),sp))
        c.close()
        xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")

#--------------------更改--------------------
    if(xz=="4"):
        gg=input("请输入你要更改的商品编码")
        while(gg!=""):
            goods1=input("请输入商品名称:")
            goods2=input("请输入商品价格:")
            goods3=int(input("请输入商品数量:"))
            ls.append(goods1)
            ls.append(goods2)
            ls.append(goods3)
            d[gg]=ls
            print(d[gg])
            ls=[]
            gg=input("请输入你要更改的商品编码")
        xz=input("请选择你要用的功能1.增加商品 2.删除商品 3.查询商品 4.更改商品 5.统计商品 6.收银 7.退出")







