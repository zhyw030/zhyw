import turtle as t
import time

# 关闭自动更新，避免闪烁，后续手动更新画面
t.tracer(0)

# 设置窗口大小和背景颜色
win_width = 800
win_height = 600
t.setup(win_width, win_height)
t.bgcolor("white")

# 定义字体样式，用于显示文字
FONT = ("Arial", 16, "normal")


# 普通条形进度条类
class BarProgressBar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.progress = 0
        # 用于绘制进度条
        self.bar_turtle = t.Turtle()
        self.bar_turtle.penup()
        self.bar_turtle.hideturtle()
        # 用于显示百分比
        self.text_turtle = t.Turtle()
        self.text_turtle.penup()
        self.text_turtle.hideturtle()

    def update(self, increment):
        
        self.progress += increment
        if self.progress > 100:
            self.progress = 100

        # 清除之前绘制内容
        self.bar_turtle.clear()
        self.text_turtle.clear()

        # 绘制进度条外框（灰色）
        self.bar_turtle.goto(self.x, self.y)
        self.bar_turtle.pendown()
        self.bar_turtle.color("gray")
        self.bar_turtle.begin_fill()
        for _ in range(2):
            self.bar_turtle.forward(self.width)
            self.bar_turtle.right(90)
            self.bar_turtle.forward(self.height)
            self.bar_turtle.right(90)
        self.bar_turtle.end_fill()
        self.bar_turtle.penup()

        # 绘制进度条填充部分（蓝色）
        filled_width = (self.width * self.progress) / 100
        self.bar_turtle.goto(self.x, self.y)
        self.bar_turtle.pendown()
        self.bar_turtle.color("blue")
        self.bar_turtle.begin_fill()
        self.bar_turtle.forward(filled_width)
        self.bar_turtle.right(90)
        self.bar_turtle.forward(self.height)
        self.bar_turtle.right(90)
        self.bar_turtle.forward(filled_width)
        self.bar_turtle.right(180)
        self.bar_turtle.end_fill()
        self.bar_turtle.penup()

        # 显示百分比文本
        self.text_turtle.goto(self.x + self.width / 2, self.y - 20)
        self.text_turtle.write(f"{self.progress}%", align="center", font=FONT)

        # 手动更新画面
        t.update()


# 带三角形的条形进度条类
class TriangularBarProgressBar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.progress = 0
        # 用于绘制进度条和三角形
        self.bar_turtle = t.Turtle()
        self.bar_turtle.penup()
        self.bar_turtle.hideturtle()
        # 用于显示百分比
        self.text_turtle = t.Turtle()
        self.text_turtle.penup()
        self.text_turtle.hideturtle()

    def update(self, increment):
        """更新带三角形的条形进度条的进度、绘制进度条和显示百分比"""
        self.progress += increment
        if self.progress > 100:
            self.progress = 100

        # 清除之前绘制内容
        self.bar_turtle.clear()
        self.text_turtle.clear()

        # 绘制进度条外框（灰色）
        self.bar_turtle.goto(self.x, self.y)
        self.bar_turtle.pendown()
        self.bar_turtle.color("gray")
        self.bar_turtle.begin_fill()
        for _ in range(2):
            self.bar_turtle.forward(self.width)
            self.bar_turtle.right(90)
            self.bar_turtle.forward(self.height)
            self.bar_turtle.right(90)
        self.bar_turtle.end_fill()
        self.bar_turtle.penup()

        # 绘制进度条填充部分（蓝色）
        filled_width = (self.width * self.progress) / 100
        self.bar_turtle.goto(self.x, self.y)
        self.bar_turtle.pendown()
        self.bar_turtle.color("blue")
        self.bar_turtle.begin_fill()
        self.bar_turtle.forward(filled_width)
        self.bar_turtle.right(90)
        self.bar_turtle.forward(self.height)
        self.bar_turtle.right(90)
        self.bar_turtle.forward(filled_width)
        self.bar_turtle.right(180)
        self.bar_turtle.end_fill()
        self.bar_turtle.penup()

        # 根据进度绘制三角形（在进度条右侧显示）
        if self.progress > 0:
            triangle_side_length = 10  # 三角形边长
            triangle_x = self.x + filled_width
            triangle_y = self.y + self.height / 2
            self.bar_turtle.goto(triangle_x, triangle_y)
            self.bar_turtle.pendown()
            self.bar_turtle.begin_fill()
            for _ in range(3):
                self.bar_turtle.forward(triangle_side_length)
                self.bar_turtle.right(120)
            self.bar_turtle.end_fill()
            self.bar_turtle.penup()

        # 显示百分比文本
        self.text_turtle.goto(self.x + self.width / 2, self.y - 20)
        self.text_turtle.write(f"{self.progress}%", align="center", font=FONT)

        # 手动更新画面
        t.update()


# 主函数，控制进度条动图的展示流程
def main():
    t.penup()
    t.hideturtle()

    # 显示“正在载入”提示
    t.goto(0, 0)
    t.write("正在载入", align="center", font=FONT)

    # 创建普通条形进度条实例并更新进度
    bar_progress_bar = BarProgressBar(-300, 100, 400, 30)
    # 创建带三角形的条形进度条实例并更新进度
    triangular_bar_progress_bar = TriangularBarProgressBar(200, 100, 400, 30)

    for i in range(0, 101, 5):
        bar_progress_bar.update(5)
        triangular_bar_progress_bar.update(5)
        time.sleep(0.1)

    # 显示“载入完成”提示，并清除“正在载入”文字
    t.goto(0, 0)
    t.clear()
    t.write("载入完成", align="center", font=FONT)

    t.done()


if __name__ == "__main__":
    main()
