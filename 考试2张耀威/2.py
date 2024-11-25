import turtle as t
t.speed(0)
t.hideturtle()
t.color("red")
x=[-200,-190,190,-180,180,-90,90,0]
y=[-300,290,-290,215,-235,120,40,-40,-200]
def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
yd(x[0],y[0])
for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(600)
    t.left(90)
t.pensize(3)
#正7
yd(x[1],y[1])
t.forward(20)
t.right(110)
t.forward(40)
t.setheading(0)
#倒7
yd(x[2],y[2])
t.forward(-20)
t.left(70)
t.forward(40)
t.setheading(0)
#画菱形
def lx(x,y,dx):
    yd(x,y)
    t.begin_fill()
    for i in range(2):
        t.left(60)
        t.forward(dx)
    t.left(120)
    t.forward(dx)
    t.left(60)
    t.forward(dx)
    t.end_fill()
    t.setheading(0)
#小菱形
lx(x[3],y[3],17)
lx(x[4],x[4],17)
#大菱形
lx(x[5],y[5],50)#1
lx(x[6],y[5],50)#2
lx(x[7],y[6],50)#3
lx(x[5],y[7],50)#4
lx(x[6],y[7],50)#5
lx(x[5],y[8],50)#6
lx(x[6],y[8],50)#7





