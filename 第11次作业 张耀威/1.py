
a="0"
while(a!="8"):
    print("\n--------欢迎使用xxxxxxx系统------")
    print("请选择你需要进行的操作(输入对应数字)")
    print("     1.功能一")
    print("     2.功能二")
    print("     3.功能三")
    print("     4.功能四")
    print("     5.功能五")
    print("     6.功能六")
    print("     7.功能七")
    print("     8.退出操作")
    a=input("请输入你的选择")


#-----------课程作业1   求年龄------------#

    def age(n):
        if(n==1):
            return 10
        else:
            return age(n-1)+2
    if(a=="1"):
        print("以进入功能一")
        t=age(5)
        print(t)
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")
#-----------课程作业2   猴子吃桃--------#

    def ts(n):
        if(n==10):
            return 1
        else:
            return 2*(ts(n+1)+1)
    if(a=="2"):
        print("以进入功能二")
        a=ts(1)
        print("桃子总数为：%d"%a)
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")
#-----------课程作业3   求5！-----------#

    def zc(n):
        if(n==1):
            return 1
        else:
            return zc(n-1)*n
    if(a=="3"):
        print("以进入功能三")
        b=zc(5)
        print(b)
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")
#------------课程作业4 求斐波那契数列的第15个数----#

    def sl(n):
        if(n==1):
            return 1
        elif(n==2):
            return 1
        else:
            return sl(n-1)+sl(n-2)
    if(a=="4"):
        print("以进入功能四")
        c=sl(15)
        print(c)
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")
#-------------课程作业5 求分数递推-------#

    def fs(n):
        if(n==1):
            return 1
        else:
            return fs(n-1)+1/(n*2-1)
    if(a=="5"):
        print("以进入功能五")
        d=fs(6)
        print("{:.4f}".format(d))
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")
#-------------课程作业6 递归求值---------#

    def qz(n):
        if(n==1):
            return 1
        elif(n%2==1):
            return qz(n-1)+(n*2-1)
        elif(n%2==0):
            return qz(n-1)-(n*2-1)

    if(a=="6"):
        print("以进入功能六")
        e=qz(8)
        print(e)
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")
#-------------课程作业7 递归求分数-------#

    def qh(n):
        if(n==1):
            return 1
        elif(n%2==1):
            return qh(n-1)+1/(n*2-1)
        elif(n%2==0):
            return qh(n-1)-1/(n*2-1)
    if(a=="7"):
        print("以进入功能七")
        f=qh(7)
        print("{:.4f}".format(f))
        print("请选择你还要进行的操作(输入对应数字)")
        print("     1.功能一")
        print("     2.功能二")
        print("     3.功能三")
        print("     4.功能四")
        print("     5.功能五")
        print("     6.功能六")
        print("     7.功能七")
        print("     8.退出操作")
        a=input("请输入你的选择")


