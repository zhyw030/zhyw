import turtle as t
t.speed(0)
t.pensize(2)
t.hideturtle()
face1=[100]
eye1=[15,10]
bc=[50,120]

#画脸
def face(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange")
    t.circle(98)
    t.hideturtle()
    t.begin_fill()
    t.circle(98)
    t.color("#ffff00")
    t.end_fill()
    
#画单只眼睛
def eyez(x1,y1):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    
    t.begin_fill()
    t.color("#ffffff")
    t.circle(eye1[0])
    t.end_fill()
    t.begin_fill()
    t.color("black")
    t.circle(eye1[1])
    t.end_fill()
def mb(x1,y1):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.color("orange")
    t.circle(eye1[0])
def eye(x1,y1):
    eyez(x1,y1)
    mb(x1,y1)
#一双眼睛
def eyes(x2,y2):
    eye(x2,y2)
    eye(x2+75,y2)
#画眼睛加脸
def a(x3,y3):
    face(0+x3,0+y3)
    eyes(-38+x3,130+y3)
#笑嘴
def b(x4,y4):
    t.color("black")
    t.penup()
    t.goto(x4-40,y4+20)
    t.pendown()
    t.setheading(-60)
    t.circle(bc[0],bc[1])
    t.setheading(0)
#笑脸
"""a(0,0)
b(0,50)"""
#转移
def zy(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#盾牌表面
def dpbm(x1,y1):
    zy(0+x1,0+y1)
    t.begin_fill()
    t.color("blue")
    t.circle(face1[0])
    t.end_fill()
    zy(0+x1,0+y1)
    t.color("red")
    t.pensize(20)
    t.circle(101)
    zy(0+x1,-40+y1)
    t.color("red")
    t.circle(140)
dpbm(0,0)
#五角星
t.pensize(0)
t.color("white")
t.penup()
t.goto(-87,125)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(175)
    t.right(180-36)
t.end_fill()
dpbm(200,200)
#笑脸
t.pensize(2)
a(200,203)
b(200,250)




    
