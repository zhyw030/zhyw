import random as r
import turtle as t
t.hideturtle()
t.speed(0)
pk=['红心A','红心2','红心3','红心4','红心5','红心6','红心7','红心8', '红心9','红心10','红心J','红心Q','红心K',
'黑桃A','黑桃2','黑桃3', '黑桃4','黑桃5','黑桃6','黑桃7','黑桃8', '黑桃9','黑桃10','黑桃J', '黑桃Q','黑桃K',
'方块A','方块2','方块3','方块4','方块5','方块6','方块7','方块8', '方块9','方块10','方块J','方块Q','方块K',
'梅 花A','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8', '梅花9','梅花10','梅花J','梅花Q','梅花K',
'小 王','大 王']
def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def pm(x,y):
    yd(x,y)
    for i in range(2):
        t.forward(70)
        t.right(90)
        t.forward(90)
        t.right(90)
def zt(x,y,nr):
    pm(0+x,0+y)
    yd(5+x,-40+y)
    t.write(nr,font=("微软雅黑", 15, "normal"))
dz=[]
nm1=[]
nm2=[]
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
    del pk[num]














