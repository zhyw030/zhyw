import random as r
import turtle as t
t.hideturtle()
t.speed(0)
pk=['红心 A 48','红心 2 52','红心 3  4','红心 4  8','红心 5 12','红心 6 16','红心 7 20','红心 8 24', '红心 9 28','红心10 32','红心 J 36','红心 Q 40','红心 K 44',
'黑桃 A 47','黑桃 2 51','黑桃 3  3', '黑桃 4  7','黑桃 5 11','黑桃 6 15','黑桃 7 19','黑桃 8 23', '黑桃 9 27','黑桃10 31','黑桃 J 35', '黑桃 Q 39','黑桃 K 43',
'方块 A 46','方块 2 50','方块 3  2','方块 4  6','方块 5 10','方块 6 14','方块 7 18','方块 8 22', '方块 9 26','方块10 30','方块 J 34','方块 Q 38','方块 K 42',
'梅花 A 45','梅花 2 49','梅花 3  1','梅花 4  5','梅花 5  9','梅花 6 13','梅花 7 17','梅花 8 21', '梅花 9 25','梅花10 29','梅花 J 33','梅花 Q 37','梅花 K 41',
'  小王 54','  大王 53']
dz=[]
nm1=[]
nm2=[]
def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def pm(x,y):
    yd(x,y)
    for i in range(2):
        t.color("grey","white")
        t.begin_fill()
        t.forward(65)
        t.circle(5,90)
        t.forward(90)
        t.circle(5,90)
        t.end_fill()
        
def zt(x,y):
    pm(x,y)
    yd(x+5,y+30)


for i in range(17):
    num=r.randint(0,len(pk)-1)
    dz.append(pk[num])
    
    del pk[num]
    num=r.randint(0,len(pk)-1)
    nm1.append(pk[num])
    
    del pk[num]
    num=r.randint(0,len(pk)-1)
    nm2.append(pk[num])
    
    del pk[num]
for j in range(1,4): 
    num=r.randint(0,len(pk)-1)
    dz.append(pk[num])
    del pk[num]

for j in range(90):
    for i in range(0,len(dz)-1 ):
        a=int(dz[i][5:7])
        b=int(dz[i+1][5:7])
        if(a<b):
            dz[i],dz[i+1]=dz[i+1],dz[i]
for j in range(90):
    for i in range(0,len(nm1)-1 ):
        a=int(nm1[i][5:7])
        b=int(nm1[i+1][5:7])
        if(a<b):
            nm1[i],nm1[i+1]=nm1[i+1],nm1[i]
for j in range(90):
    for i in range(0,len(nm2)-1 ):
        a=int(nm2[i][5:7])
        b=int(nm2[i+1][5:7])
        if(a<b):
            nm2[i],nm2[i+1]=nm2[i+1],nm2[i]
#print(dz,nm1,nm2)
for i in range(17):
    #---------------地主---------
    zt(-600+i*35,245)
    if(dz[i][0:2]=="红心"):
        t.color("red")
        t.write('\u2665',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35,300)
        t.write(dz[i][2:4],font=("微软雅黑", 15, "normal"))
    if(dz[i][0:2]=="黑桃"):
        t.color("black")
        t.write('\u2660',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35,300)
        t.write(dz[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(dz[i][0:2]=="方块"):
        t.color("red")
        t.write('\u2666',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35,300)
        t.write(dz[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(dz[i][0:2]=="梅花"):
        t.color("black")
        t.write('\u2663',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35,300)
        t.write(dz[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(dz[i][2:4]=="小王"):
        t.color("black")
        yd(-600+i*35,320)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-602+i*35,300)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35,280)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35,260)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35,240)
        t.write("R",font=("微软雅黑", 10, "normal"))
    if(dz[i][2:4]=="大王"):
        t.color("red")
        yd(-600+i*35,320)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-602+i*35,300)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35,280)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35,260)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35,240)
        t.write("R",font=("微软雅黑", 10, "normal"))
    #---------------农民1——————————
    zt(-400+i*35,100)
    if(nm1[i][0:2]=="红心"):
        t.color("red")
        t.write('\u2665',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,155)
        t.write(nm1[i][2:4],font=("微软雅黑", 15, "normal"))
    if(nm1[i][0:2]=="黑桃"):
        t.color("black")
        t.write('\u2660',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,155)
        t.write(nm1[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(nm1[i][0:2]=="方块"):
        t.color("red")
        t.write('\u2666',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,155)
        t.write(nm1[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(nm1[i][0:2]=="梅花"):
        t.color("black")
        t.write('\u2663',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,155)
        t.write(nm1[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(nm1[i][2:4]=="小王"):
        t.color("black")
        yd(-400+i*35,175)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-402+i*35,155)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,135)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,115)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,95)
        t.write("R",font=("微软雅黑", 10, "normal"))
    if(nm1[i][2:4]=="大王"):
        t.color("red")
        yd(-400+i*35,175)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-402+i*35,155)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,135)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,115)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,95)
        t.write("R",font=("微软雅黑", 10, "normal"))
#------------------农民2----------------
    zt(-400+i*35,0)
    if(nm2[i][0:2]=="红心"):
        t.color("red")
        t.write('\u2665',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,55)
        t.write(nm2[i][2:4],font=("微软雅黑", 15, "normal"))
    if(nm2[i][0:2]=="黑桃"):
        t.color("black")
        t.write('\u2660',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,55)
        t.write(nm2[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(nm2[i][0:2]=="方块"):
        t.color("red")
        t.write('\u2666',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,55)
        t.write(nm2[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(nm2[i][0:2]=="梅花"):
        t.color("black")
        t.write('\u2663',font=("微软雅黑", 20, "normal"))
        yd(-400+i*35,55)
        t.write(nm2[i][2:4],font=("微软雅黑", 15, "normal")) 
    if(nm2[i][2:4]=="小王"):
        t.color("black")
        yd(-400+i*35,75)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-402+i*35,55)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,35)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,15)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,-5)
        t.write("R",font=("微软雅黑", 10, "normal"))
    if(nm2[i][2:4]=="大王"):
        t.color("red")
        yd(-400+i*35,75)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-402+i*35,55)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,35)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,15)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-400+i*35,-5)
        t.write("R",font=("微软雅黑", 10, "normal"))
for j in range(1,4):
    zt(-600+i*35+j*35,245)
    if(dz[i+j][0:2]=="红心"):
        t.color("red")
        t.write('\u2665',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35+j*35,300)
        t.write(dz[i+j][2:4],font=("微软雅黑", 15, "normal"))
    if(dz[i+j][0:2]=="黑桃"):
        t.color("black")
        t.write('\u2660',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35+j*35,300)
        t.write(dz[i+j][2:4],font=("微软雅黑", 15, "normal")) 
    if(dz[i+j][0:2]=="方块"):
        t.color("red")
        t.write('\u2666',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35+j*35,300)
        t.write(dz[i+j][2:4],font=("微软雅黑", 15, "normal")) 
    if(dz[i+j][0:2]=="梅花"):
        t.color("black")
        t.write('\u2663',font=("微软雅黑", 20, "normal"))
        yd(-600+i*35+j*35,300)
        t.write(dz[i+j][2:4],font=("微软雅黑", 15, "normal")) 
    if(dz[i+j][2:4]=="小王"):
        t.color("black")
        yd(-600+i*35+j*35,320)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-602+i*35+j*35,300)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35+j*35,280)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35+j*35,260)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35+j*35,240)
        t.write("R",font=("微软雅黑", 10, "normal"))
    if(dz[i+j][2:4]=="大王"):
        t.color("red")
        yd(-600+i*35+j*35,320)
        t.write("J",font=("微软雅黑", 10, "normal"))
        yd(-602+i*35+j*35,300)
        t.write("O",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35+j*35,280)
        t.write("K",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35+j*35,260)
        t.write("E",font=("微软雅黑", 10, "normal"))
        yd(-600+i*35+j*35,240)
        t.write("R",font=("微软雅黑", 10, "normal"))


















