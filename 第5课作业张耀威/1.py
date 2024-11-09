import turtle as t
t.speed(0)
t.pensize(1)
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
def eye(x1,y1):
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
    t.color("orange")
    t.circle(eye1[0])

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
a(200,0)
c(200,0)



    



