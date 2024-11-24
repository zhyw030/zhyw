import random as r
x=int(input("你要开始游戏吗?1.是 2.否"))
while(x!=2):
    if(x==1):
        print("现在游戏即将开始，你有9次机会猜，机会用完游戏结束")
        a=r.randint(1,99)
        n=9
        print(a)
        while(n!=0):
            b=int(input("请输入你猜数字为多少"))
            if(b==a and n==9):
                print("哇！你是不是开桂了，一发入魂！")
                n=0
            elif(b==a and n>=6):
                print("这么快就猜对了，你真的太棒了！")
                n=0
            elif(b==a and 0<n<6):
                print("不错嘛，居然猜出来了。")
                n=0
            elif(b!=a):
                if(b>a):
                    n=n-1
                    if(n==0):
                        print("游戏结束了，你没有猜对")
                        
                    else:
                        print("你猜的数大了，猜小一点试试")
                        print("你还有{}次机会".format(n))
                if(b<a):
                    n=n-1
                    if(n==0):
                        print("游戏结束了，你没有猜对")
                    else:
                        print("你猜的数小了，猜大一点试试")
                        print("你还有{}次机会".format(n))    
        x=int(input("你要再来一次吗?1.是 2.否"))





