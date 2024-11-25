import turtle as t
t.speed(0)
t.hideturtle()
a=input("请输入名字")
b=input("请输入社团名")
c=input("请输入QQ号")
d=input("请输入slogan")
#lr1=["张耀威","2024编程实验室","3185687003","努力沉淀，不做没有理想的咸鱼"]
def yd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown
t.color("#808080")
t.begin_fill()
yd(-100,-200)
for i in range(2):
    t.forward(700)
    t.left(90)
    t.forward(400)
    t.left(90)
t.end_fill()
#画字
def hz(x1,y1,lr,dx):
    t.color("black")
    yd(x1,y1)
    t.write(lr,font=("cmr10",dx,"normal"))
hz(100,-50,a,70)
hz(-50,100,b,30)
hz(400,-10,"QQ",20)
hz(380,-40,c,20)
hz(50,-100,d,25)


