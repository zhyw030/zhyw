import math as m
import random as r
a=input("请选择你要计算的方式  1.方法1 2.方法2 3.方法3 4.退出")
while(a!=4):
    if(a=="1"):
        print("已经启动方法1")
        sz=0
        for i in range(100):
            sz+=1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
        print("Π值是{:.10f}".format(sz))
        a=input("请选择你要计算的方式  1.方法1 2.方法2 3.方法3 4.退出")
    elif(a=="2"):
        print("已经启动方法2")
        sz,n,fh,zh=0,1,1,1
        while(m.fabs(zh)>=10**-6):
            sz+=zh
            n+=2
            fh=-fh
            zh=fh/n
        sz=sz*4
        print("Π值是{:.10f}".format(sz))
        a=input("请选择你要计算的方式  1.方法1 2.方法2 3.方法3 4.退出")
    elif(a=="3"):
        print("已经启动方法3")
        dz=1000*1000
        hits=0.0
        for i in range(dz):
            x,y=r.random(),r.random()
            dist=pow(x**2+y**2,0.5)
            if(dist<=1.0):
                hits+=1.0
        pai=4*(hits/dz)
        print("Π值是{}".format(pai))
        a=input("请选择你要计算的方式  1.方法1 2.方法2 3.方法3 4.退出")

