import turtle
turtle.speed(50)
#画大五角星
def a(x1,y2):
    turtle.left(90)
    turtle.color("#e0e254")
    turtle.penup()
    turtle.goto(-420+x1,180+160/15+y2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(180-36)
    turtle.forward(200)
    turtle.right(180-36)
    turtle.forward(200)
    turtle.right(180-36)
    turtle.forward(200)
    turtle.right(180-36)
    turtle.forward(200)
    turtle.end_fill()
#小五角星1
def b(x4,y4):
    turtle.right(90)
    turtle.color("#e0e254")
    turtle.penup()
    turtle.goto(-210+160/3+x4,220+160/5+y4)
    turtle.pendown()
#小五角星2
def d(x5,y5):
    turtle.right(20)
    turtle.penup()
    turtle.goto(-430+380+x5,180+20+y5)
    turtle.pendown()
    
#画小星星
def c():
    turtle.begin_fill()
    turtle.forward(60)
    turtle.right(180-36)
    turtle.forward(60)
    turtle.right(180-36)
    turtle.forward(60)
    turtle.right(180-36)
    turtle.forward(60)
    turtle.right(180-36)
    turtle.forward(60)
    turtle.end_fill()

#五星红旗底部
def e(x6,y6):
    turtle.color("#ea111c")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-480+x6,-320+y6)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(960)
    turtle.left(90)
    turtle.forward(640)
    turtle.left(90)
    turtle.forward(960)
    turtle.left(90)
    turtle.forward(640)
    turtle.end_fill()
            


e(0,0)       
a(0,0)
b(0,0)
c()
b(0,-210)
c()
d(0,30)
c()
d(-50,-60)
c()




    
