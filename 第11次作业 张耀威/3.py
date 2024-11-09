def move(n,x,y,z):    #n为汉诺塔数，x为初始柱子，y为中转柱子，z为目标柱子
    if(n>0):
        move(n-1,x,z,y)
        print("移动盘子",n,"从",x,"到",y)
        move(n-1,z,y,x)
while(1):
    a=int(input("请输入汉诺塔的层数"))
    move(a,"起点","终点","中转")
