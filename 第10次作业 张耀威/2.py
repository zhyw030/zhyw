import turtle as t

def draw_circle(localx, localy, r, extent, framecolor, fillcolor):  # 初始x位置，初始y位置，半径，角度，边框颜色，填充颜色
    t.up()
    t.goto(localx, localy)
    t.color(framecolor)
    t.down()
    t.begin_fill()
    t.circle(r, extent)
    t.color(fillcolor)
    t.end_fill()
    t.seth(0)

def draw_juxing(frame_color,fill_color,localx,localy,len,wid,r):
    t.color(frame_color)
    t.seth(0)
    t.left(90)
    t.up()
    t.goto(localx,localy)
    t.down()
    t.begin_fill()
    t.forward(wid)
    t.circle(r,90)
    t.forward(len)
    t.circle(r,90)
    t.forward(wid)
    t.circle(r,90)
    t.forward(len)
    t.circle(r,90)
    t.color(fill_color)
    t.end_fill()
    t.seth(0)

def main():
    t.speed(0)
    t.hideturtle()
    draw_juxing('black','#a8a8a8',430,-150,800,300,30)
    draw_juxing('red', 'red', 430, -150, 30, 300, 0)
    draw_juxing('red', 'red', -400, -150, 30, 300, 0)
    draw_juxing('red', 'red', 400, 150, 800, 30, 0)
    draw_juxing('red', 'red', 400, -180, 800, 30, 0)
    draw_juxing('#006400', '#006400', 400, -150, 800, 300, 0)

    draw_circle(400,-165,15,360,'#7f7f7f','#7f7f7f')
    draw_circle(400, 135, 15, 360, '#7f7f7f', '#7f7f7f')
    draw_circle(-400, -165, 15, 360, '#7f7f7f', '#7f7f7f')
    draw_circle(-400, 135, 15, 360, '#7f7f7f', '#7f7f7f')
    t.seth(0)
    t.left(90)
    draw_circle(-15, 149, -15, 180, '#7f7f7f', '#7f7f7f')
    t.seth(0)
    t.right(90)
    draw_circle(15, -150, -15, 180, '#7f7f7f', '#7f7f7f')

    t.color('black')
    t.width(2)

    t.seth(0)
    t.right(90)
    t.up()
    t.goto(-200,150)
    t.down()
    t.forward(300)

    t.seth(0)
    t.up()
    t.goto(-200,-50)
    t.down()
    t.circle(50,-180)


    t.seth(0)
    draw_circle(-250,-10,10,360,'white','white')
    draw_circle(-200, -10, 10, 360, 'orange', 'orange')
    draw_circle(-200, -60, 10, 360, 'yellow', 'yellow')
    draw_circle(-200, 40, 10, 360, '#008000', '#008000')
    draw_circle(30, -10, 10, 360, '#0000ff', '#0000ff')
    draw_circle(130, -10, 10, 360, 'white', 'white')
    draw_circle(320, -10, 10, 360, 'black', 'black')

    lx = 180
    ly = -10
    for i in range(1,6):
        y = ly
        for j in range(i):

            draw_circle(lx,y,10,360,'red','red')
            y+=20
        lx+=20
        ly-=10


    t.mainloop()

if __name__ == '__main__':
    main()
