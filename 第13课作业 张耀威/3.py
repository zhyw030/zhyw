import turtle as t
import time
import random
#-----------------------图案列表-------------------------------
ls=[#   1            2           3           4           5           6           7           8           9           10
    '\u264B'  ,  '\u2648',   '\u2649',   '\u264F',   '\u264E',   '\u264A',   '\u264D',   '\u2653',   '\u264C',   '\u264F',#1
    
    '\u2653'  ,  '\u264F',   '\u264B',   '\u2648',   '\u2649',   '\u264F',   '\u264E',   '\u264C',   '\u264E',   '\u264A',#2
    
    '\u2648'  ,  '\u2649',   '\u264F',   '\u2653',   '\u264B',   '\u264E',   '\u264C',   '\u264A',   '\u2652',   '\u264B',#3
    
    '\u264D'  ,  '\u2650',   '\u2652',   '\u264B',   '\u2649',   '\u264C',   '\u2648',   '\u264F',   '\u264A',   '\u264F',#4
    
    '\u264A'  ,  '\u2649',   '\u264B',   '\u2652',   '\u264C',   '\u264F',   '\u2653',   '\u2648',   '\u2653',   '\u2649',#5
    
    '\u2649'  ,  '\u264D',   '\u264F',   '\u264C',   '\u2648',   '\u2650',   '\u264E',   '\u2651',   '\u264E',   '\u264C',#6
    
    '\u2652'  ,  '\u2649',   '\u264C',   '\u2648',   '\u264B',   '\u264A',   '\u2650',   '\u264F',   '\u264E',   '\u264D',#7
    
    '\u264E'  ,  '\u264C',   '\u2648',   '\u2649',   '\u264F',   '\u264B',   '\u264F',   '\u2653',   '\u264D',   '\u264E',#8
    
    '\u264C'  ,  '\u264F',   '\u264E',   '\u264D',   '\u2648',   '\u2649',   '\u264B',   '\u2652',   '\u264F',   '\u264C',#9

    '\u264D'  ,  '\u2650',   '\u2652',   '\u264B',   '\u2649',   '\u264C',   '\u2648',   '\u264F',   '\u2653',   '\u264A'#10    
    ]
#----------------------定位数据----------------------
X_title,Y_title=-540,200    #标题的起点位置
X_frame,Y_frame=5,325      #方框的起点位置
X_shape,Y_shape=-45,280     #图案与文字的起点位置
X_ball,Y_ball=-320,-150     #水晶球的位置
X_ruler,Y_ruler=-580,-230   #规则文字的位置  -380,-70


#定义goto，方便使用
def goto(x,y):
    t1.pu()
    t1.goto(x,y)
    t1.pd()    
#显示标题并初始显示
def begin():          
    t.bgcolor ('aqua')
    t1.speed(0)
    t1.hideturtle()
    goto(X_title,Y_title)
    t1.write('吉普赛读心术',font=('楷体',60))
#图表框架
def frame():
    for q in range(0,11):        
        goto(X_frame,Y_frame-q*55)#横线
        t1.seth(0)
        t1.fd(600)
        goto(X_frame+q*60,Y_frame)#纵线
        t1.seth(-90)
        t1.fd(550)
        t1.seth(0)        
#图和数字序号        
def chart():
    frame()    
    goto(X_shape,Y_shape)
    for j in range(1,11):
        for i in range(((j-1)*10),j*10):
            t1.pencolor('red')
            t1.pu()
            t1.fd(60)
            t1.pd()        #拉间隔
            t1.write(ls[i],font=('楷体',30))#画图案
            t1.penup()
            t1.right(90)
            t1.fd(10)
            t1.left(90)
            t1.fd(15)
            t1.pendown()   #数字显示找位置
            t1.pencolor('black')
            t1.write(i+1,font=('French Script MT',14))  #标数字
            #t1.fd(3)
            #t1.circle(27)
            #t1.fd(-3)
            t1.penup()
            t1.fd(-15)
            t1.left(90)
            t1.fd(10)
            t1.right(90)
            t1.pendown()   #画笔归位    
        t1.pu()
        t1.goto(X_shape,Y_shape-j*55)
        t1.pd()            #向下移一行    
#水晶球
def ball():
    goto(X_ball,Y_ball)
    t1.pensize(10)
    t1.color('purple3','purple1')
    t1.begin_fill()
    t1.circle(150)
    t1.end_fill()

#游戏规则--------------------------------------------------
def word():
    goto(X_ruler,Y_ruler)
    t1.write('游戏规则：\n请想10-99中任意一个数：',font=('华文彩云',20))
    goto(X_ruler,Y_ruler-40)
    t1.write('将这个数减去个位，再减去十位,并且在列表中找到结果对应的符号',font=('华文彩云',20))
    goto(X_ruler,Y_ruler-2*40)
    t1.write('请把这个符号记在心中,准备好被看穿内心了吗？请点击水晶球！',font=('华文彩云',20))
#作图-------------------------------------------------------
def draw():
    begin()
    chart()
    ball()
    word()    

#显示操作---------------------------------------------------

def a(x,y):         # 一旦屏幕点击，本程序就运行图案
    t1.color("yellow")
    goto(X_ruler+180,Y_ruler+150)  #相对球的位置偏移一下
    t1.write(ls[8],font=('楷体',120))
def control():
    t.onscreenclick(a)#启动屏幕点击侦测功能    


#-----------------------图元素---------------------------------
#定义两支画笔
t.tracer(0)#无轨迹显示法
t1=t.Pen()	
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()
#数据乱序
random.shuffle(ls)
for i in range(10):
    ls[i*9-1]=ls[8]

#最后运行----------------------------------------------------

draw()    
control()            
t.tracer(1)   #与t.tracer(0)呼应，否则会显示不完整 
