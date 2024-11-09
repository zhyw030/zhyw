import random as r
import turtle as t
t.hideturtle()
t.speed(0)
pk=['红心 A','红心 2','红心 3','红心 4','红心 5','红心 6','红心 7','红心 8', '红心 9','红心10','红心 J','红心 Q','红心 K',
'黑桃 A','黑桃 2','黑桃 3', '黑桃 4','黑桃 5','黑桃 6','黑桃 7','黑桃 8', '黑桃 9','黑桃10','黑桃 J', '黑桃 Q','黑桃 K',
'方块 A','方块 2','方块 3','方块 4','方块 5','方块 6','方块 7','方块 8', '方块 9','方块10','方块 J','方块 Q','方块 K',
'梅花 A','梅花 2','梅花 3','梅花 4','梅花 5','梅花 6','梅花 7','梅花 8', '梅花 9','梅花10','梅花 J','梅花 Q','梅花 K',
'  小王','  大王']
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







    
#t.write(,font=("微软雅黑", 50, "normal"))
for i in range(17):
    num=r.randint(0,len(pk)-1)
    dz.append(pk[num])
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
    del pk[num]

    num=r.randint(0,len(pk)-1)
    nm1.append(pk[num])
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
    del pk[num]
    
    num=r.randint(0,len(pk)-1)
    nm2.append(pk[num])
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
    del pk[num]

       

for j in range(1,4): 
    num=r.randint(0,len(pk)-1)
    dz.append(pk[num])
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
    del pk[num]
"""t.color("black")
yd(-598,310)
t.write("J",font=("微软雅黑", 10, "normal"))
yd(-600,295)
t.write("O",font=("微软雅黑", 10, "normal"))
yd(-598,280)
t.write("K",font=("微软雅黑", 10, "normal"))
yd(-598,245)
t.write("E",font=("微软雅黑", 10, "normal"))
yd(-598,230)
t.write("R",font=("微软雅黑", 10, "normal"))"""
















    
"""
for i in range(17):
    num=r.randint(0,len(pk)-1)
    dz.append(pk[num])
    zt(-600+i*70,200,dz[i])
    del pk[num]
    num=r.randint(0,len(pk)-1)
    nm1.append(pk[num])
    zt(-400+i*70,100,nm1[i])
    del pk[num]
    num=r.randint(0,len(pk)-1)
    nm2.append(pk[num])
    zt(-400+i*70,0,nm2[i])
    del pk[num]
for j in range(1,4): 
    num=r.randint(0,len(pk)-1)
    dz.append(pk[num])
    zt(-600+i*70+j*70,200,dz[i+j])
    del pk[num]"""

