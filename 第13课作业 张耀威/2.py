import turtle as t
import time
def sz(x,y):
    global k
    k=1
t1=t.Pen()
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()
t.tracer(0)
t1.penup()
t2.penup()
t1.color("red")
t1.goto(-190,150)
t1.write("挑战珠穆朗玛峰",font=("楷书",60))
a=0.01
sum=8700
add=0.01
k=0
t.onscreenclick(sz)
while(1):
    time.sleep(0)
    sum+=add
    t2.goto(-20,-50)
    t2.write("{:.2f}".format(sum),align="center",font=("楷体",60))
    
    if(k==1):
        sum-=add
    t2.clear()

