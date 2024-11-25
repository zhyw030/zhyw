import turtle as t
import time
t.hideturtle()

def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#----------------箭身-----------
def js(x,y):
    yd(x,y)
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(120)
    t.forward(40)
    t.setheading(0)
    yd(200+x,-10+y)
    t.right(90)
    t.forward(20)
    t.right(120)
    t.forward(40)
    #t.clear()
    t.setheading(0)
#-----------------箭------
def zj(x,y):
    js(0+x,0+y)
    yd(0+x,0+y)
    t.left(90)
    t.forward(10)
    for j in range(2):
        t.left(120)
        t.forward(30)
    t.left(120)
    t.forward(10)
    #t.clear()
    t.setheading(0)
a=1
while(1):
    t.tracer(0)
    time.sleep(0.2)
    
    zj(-5*a,0)
    a+=1
    t.tracer(5,0)
    t.clear()
    zj(-5*a,0)
    yd(0,0)

    
    
    













