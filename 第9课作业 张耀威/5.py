a=2
while(a!=1):
    year=2024
    a=int(input("请输入多少年"))
    c=year+a
    for i in range(1,a+1):
        if((c+i)%4==0 and (c+i)%100!=0):
            print("{}是普通闰年".format(c+i))
        if((c+i)%4==0 and (c+i)%100==0):
            print("{}是世纪闰年".format(c+i))
    b=int(input("是否要在来一次  1.是  2.否"))
    if(b==1):
        a=2
    else:
        a=1














