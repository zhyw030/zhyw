import turtle
import time
turtle.speed(0)
def s():
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(24)
    turtle.right(180-36)
    turtle.forward(24)
    turtle.right(180-36)
    turtle.forward(24)
    turtle.right(180-36)
    turtle.forward(24)
    turtle.right(180-36)
    turtle.forward(24)
    turtle.end_fill()
def qz(x,y):
    #五星红旗底部
    
    turtle.color("#ea111c")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-480+x,-320+y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(96*4)
    turtle.left(90)
    turtle.forward(64*4)
    turtle.left(90)
    turtle.forward(96*4)
    turtle.left(90)
    turtle.forward(64*4)
    turtle.end_fill()
    #大五角星
    turtle.left(90)
    turtle.color("#e0e254")
    turtle.penup()
    turtle.goto(-460+x,-130+160/15+y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(80)
    turtle.right(180-36)
    turtle.forward(80)
    turtle.right(180-36)
    turtle.forward(80)
    turtle.right(180-36)
    turtle.forward(80)
    turtle.right(180-36)
    turtle.forward(80)
    turtle.end_fill()

    #小五角星1
    turtle.right(90)
    turtle.color("#e0e254")
    turtle.penup()
    turtle.goto(-425+160/3+x,-125+160/5+y)
    s()
    

    #小五角星2
    turtle.right(20)
    turtle.penup()
    turtle.goto(-375+160/3+x,-150+160/5+y)
    s()
    
    #小五角星3
    turtle.right(40)
    turtle.penup()
    turtle.goto(-385+160/3+x,-170+160/5+y)
    s()
    
    #小五角星4
    turtle.penup()
    turtle.goto(-425+160/3+x,-225+160/5+y)
    s()
    turtle.setheading(0)
#国旗杆
t1=turtle.Turtle()
t1.penup()
t1.goto(-92,-320)
t1.pendown()
t1.color("black")
t1.pensize(5)
t1.left(90)
t1.forward(900)
t1.hideturtle
t1.right(90)
#国旗
a=1
while(a!=100):
    turtle.tracer(0)
    time.sleep(0.1)
    
    t2=turtle.Turtle
    qz(0,a*5)
    a+=1
    turtle.tracer(5,0)
    turtle.clear()
qz(0,a*5)
    







