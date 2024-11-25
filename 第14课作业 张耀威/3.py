import turtle as t
#---------------------河-------------------#
t.begin_fill()
t.color("blue")
t.pu()
t.goto(200,600)
t.pendown()
t.goto(-200,600)
t.goto(-200,-600)
t.goto(200,-600)
t.goto(200,600)
t.end_fill()
t.register_shape("狼.gif")
t.register_shape("羊.gif")
t.register_shape("菜.gif")
t.register_shape("船.gif")
#------------狼-----------------#
t1=t.Turtle()
t1.shape("狼.gif")
t1.pu()
#-------------羊----------------#
t2=t.Turtle()
t2.shape("羊.gif")
t2.pu()
#------------菜-----------------#
t3=t.Turtle()
t3.shape("菜.gif")
t3.pu()
#------------船-----------------#
t4=t.Turtle()
t4.shape("船.gif")
t4.pu()
t1.goto(-300,400)       #狼
t2.goto(-300,150)       #羊
t3.goto(-300,-100)      #菜
a=1               #羊
b=-1              #狼
c=-1              #草
qd=[a,b,c]
zd=[]
def move(sz,dh,lb1,lb2,j,k):
    print(f"把{dh}从{j}运到{k}")
    i=lb1.index(sz)
    lb1.pop(i)
    lb2.append(sz)
for p in range(4):
    m=sum(qd)
    if(m==-1 or m==1 ):
        move(a,"羊",qd,zd,"起点","终点")
        t4.goto(-200,150)
        t2.hideturtle()
        t4.goto(200,150)
        t2.goto(300,150)
        t2.showturtle()
        t4.goto(0,0)

    elif(m==-2):
        move(b,"狼",qd,zd,"起点","终点")
        t4.goto(-200,400)
        t1.hideturtle()
        t4.goto(200,400)
        t1.goto(300,400)
        t1.showturtle()
        t4.goto(0,0)
    else:
        move(c,"菜",qd,zd,"起点","终点")
        t4.goto(-200,-100)
        t3.hideturtle()
        t4.goto(200,-100)
        t3.goto(300,-100)
        t3.showturtle()
        t4.goto(0,0)
    n=sum(zd)
    if(n==0):
        move(a,"羊",zd,qd,"终点","起点")
        t4.goto(200,150)
        t2.hideturtle()
        t4.goto(-200,150)
        t2.goto(-300,150)
        t2.showturtle()
        t4.goto(0,0)
print(qd,zd)




















