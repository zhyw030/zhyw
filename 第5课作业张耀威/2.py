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
    t.circle(face1[0])
    t.hideturtle()
    t.begin_fill()
    t.circle(face1[0])
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
    t.circle(50,120)
    t.setheading(0)
#哭嘴
def c(x5,y5):
    t.color("black")
    t.penup()
    t.goto(x5+40,y5+35)
    t.pendown()
    t.setheading(bc[1])
    t.circle(bc[0],bc[1])
    t.setheading(0)
#笑脸
a(0,0)
b(0,50)
#哭脸
a(200,0)
c(200,0)
#无语脸
face(200,200)
def yanjing(x6,y6,z1):
    t.penup()
    t.goto(120+x6,330+y6)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.color("orange","#ffffff")
        t.forward(55)#眼长
        t.right(90)
        t.forward(20+z1)#眼宽
        t.right(90)
    t.end_fill()
#画眼眶
def yankuang(x7,y7):
    yanjing(0+x7,0+y7,0)
    yanjing(110+x7 ,0+y7,0)
yankuang(0,0)
def yanzhu(x8,y8):
    t.penup()
    t.goto(160+x8,330+y8)
    t.pendown()
    t.setheading(90)
    t.begin_fill()
    t.color("black")
    t.circle(15,-180)#眼珠
    t.end_fill()
yanzhu(0,0)
yanzhu(110,0)
t.setheading(0)
t.penup()
t.goto(185,290)
t.pendown()
t.forward(30)
#笑脸2
def yanhei(x1,y1):
    t.penup()
    t.goto(x1,y1)
    t.pendown()   
    t.begin_fill()
    t.color("black")
    t.circle(eye1[1])
    t.end_fill()

face(0,200)
yanjing(-190,10,10)
yanjing(-100,10,10)
yanhei(-40,315)
yanhei(35,315)
t.penup()
t.goto(0,260)
t.pendown()
t.color("black")
t.circle(70,25)
t.circle(70,-50)

    



