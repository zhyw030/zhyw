import turtle as t
def zt(x,y):
    global k
    k=1

t1=t.Pen()
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()
t.tracer(0)
t1.penup()
t2.penup()
t1.color('red')
#-------------显示标题--------------#
t1.goto(-180,150)
t1.write("抢10免单",font=("楷体",60))
#--------------显示数字--------------#
sum=0.01
add=0.01
k=0
t.onscreenclick(zt)
while(1):
    sum+=add
    t2.goto(-20,-50)
    t2.write("{:.2f}".format(sum),align="center",font=("楷体",60))
    for j in range(1000):
        for i in range(321):
            pass
    if(k==1):
        sum-=add
    t2.clear()











    
