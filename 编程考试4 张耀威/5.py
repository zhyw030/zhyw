import turtle


# 设置画笔速度
turtle.speed(50)

# 定义棋盘边长
square_size = 30
board_size = 8

# 移动到起始位置
turtle.penup()
turtle.goto(-square_size * 4, square_size * 4)
turtle.pendown()

for row in range(board_size):
    for col in range(board_size):
        if (row + col) % 2 == 0:
            turtle.begin_fill()
            turtle.fillcolor("black")
        else:
            turtle.begin_fill()
            turtle.fillcolor("white")
        for _ in range(4):
            turtle.forward(square_size)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(square_size)
    turtle.penup()
    turtle.backward(square_size * board_size)
    turtle.right(90)
    turtle.forward(square_size)
    turtle.left(90)
    turtle.pendown()

turtle.done()
