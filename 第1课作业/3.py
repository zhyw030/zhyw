import datetime
a=datetime.datetime.now()
while(1):
    print("\n请输入商品名称:")
    b=input()
    print("\n请输入数量:")
    c=input()
    c=int(c)
    print("\n请输入单价:")
    d=input()
    d=float(d)
    e=c*d
    print(a)
    print("瘦西北超市(欢迎您)   收银员编号：114514")
    print("商品名称：",b,"数量:",c,"单价:",d,"总和:",e)
