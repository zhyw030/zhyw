import turtle as t
t.speed(0)
t.pensize(00)
def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#-------------------旗子面--------------------------
t.color("red")
t.begin_fill()
for j in range(2):
    t.forward(450)
    t.left(90)
    t.forward(270)
    t.left(90)
t.end_fill()
for i in range(8):
    t.pensize(20)
    t.color("white")
    t.forward(450)
    yd(0,0+i*40)
#-------------蓝色旗子面----------
t.color("#010567")
t.pensize(0)
t.begin_fill()
yd(200,i*40-10)
for j in range(2):
    t.right(90)
    t.forward(140)
    t.right(90)
    t.forward(200)
t.end_fill()
#-----------------星星------------------
def qb(x):
    for a in range(6):
        t.color("white")
        yd(180-35*a,(i-1)*40+15-x)
        t.begin_fill()
        for b in range(5):
            t.forward(15)
            t.right(180-36)
        t.end_fill()
    for a in range(6):
        t.color("white")
        yd(160-35*a,(i-2)*40+45-x)
        t.begin_fill()
        for b in range(5):
            t.forward(15)
            t.right(180-36)
        t.end_fill()
for z in range(4):
    qb(z*25)
for a in range(6):
        t.color("white")
        yd(180-35*a,(i-1)*40+15-(z+1)*25)
        t.begin_fill()
        for b in range(5):
            t.forward(15)
            t.right(180-36)
        t.end_fill()













    
