import turtle as t
t.hideturtle()
def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#-------红圈----
t.speed(0)
t.color("red")
t.pensize(10)
t.circle(95)
#---------绿圈----
t.color("green")
yd(-100,-95)
t.pensize(10)
t.circle(95)
#--------黑圈---
t.color("black")
yd(-200,0)
t.pensize(10)
t.circle(95)
#--------黄圈---
t.color("yellow")
yd(-300,-115)
t.pensize(10)
t.circle(95)
#--------蓝圈---
t.color("blue")
yd(-400,0)
t.pensize(10)
t.circle(95)
#------------红圈---
t.setheading(0)
t.color("red")
yd(0,0)
t.circle(95,-30)
#---------绿圈----
t.setheading(0)
t.color("green")
yd(-100,-95)
t.circle(95,-170)
#--------黑圈---
t.setheading(0)
t.color("black")
yd(-200,0)
t.circle(95,-30)
#--------黄圈---
t.setheading(0)
t.color("yellow")
yd(-300,-115)
t.circle(95,-190)
#--------蓝圈---
t.setheading(0)
t.color("blue")
yd(-400,0)
t.pensize(10)
t.circle(95,-300)















