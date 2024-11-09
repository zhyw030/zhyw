import turtle as t
t.speed(100)
t.hideturtle()
t.pensize(2)
d1=[-300,150]
d2=[-125]
d3=[-50]
d4=[-30]
d5=[0]
d6=[100,50]
d8=[-85]
#尾线坐标
x=[-80,120,10,100,50,250,75,200]
y=[-200,-80,-150,-5,-30,25,0]
def g(x1,y1):
    t.goto(x1,y1)
def yd(x2,y2,x3,y3):
    t.penup()
    g(x2,y2)
    t.pendown()
    g(x3,y3)
#右边翅膀
t.color("black","blue")
t.begin_fill()
g(d6[0],d6[1])
g(d1[0],d1[1])
g(d5[0],d5[0])#(0,0)
t.end_fill()
#左边翅膀
g(d4[0],d2[0])
g(d3[0],d3[0])
g(d1[0],d1[1])#(-300,150)
t.color("black","blue")
t.begin_fill()
g(d2[0],d2[0])
g(d3[0],d3[0])#(-50,-50)
t.end_fill()
t.begin_fill()
g(d4[0],d2[0])
g(d8[0],d8[0])
t.end_fill()
yd(x[0],d2[0],x[1],y[0])
yd(x[2],y[1],x[3],y[2])
yd(x[4],y[3],x[5],y[4])
yd(x[6],y[5],x[7],y[6])
t.color("red")
t.begin_fill()
yd(250,200,250,200)
t.circle(40)
t.end_fill()





