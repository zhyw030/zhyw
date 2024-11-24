import turtle as t
import random as r
import time

# 屏幕宽度和高度，设定只在屏幕上方区域显示弹幕
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BARRAGE_HEIGHT = 30  # 弹幕高度范围，可根据实际调整
BARRAGE_SPEED_MIN = 1  # 最小速度
BARRAGE_SPEED_MAX = 5  # 最大速度
BARRAGE_SIZE_MIN = 20  # 最小字号
BARRAGE_SIZE_MAX = 40  # 最大字号
TEXT_COLORS = ["red", "green", "blue", "yellow", "purple", "orange"]  # 文字颜色

# 创建barrage_text.txt文件并写入示例弹幕内容
def create_barrage_text_file():
    with open('barrage_text.txt', 'w') as file:
        file.write("OHHHHHHHH!\n")
        file.write("无敌了孩子\n")
        file.write("能赢吗？包死的\n")
        file.write("都给我玩原神\n")
        file.write("泰库辣\n")
        file.write("阿米诺斯\n")
        file.write("逆天\n")
        file.write("真是无语\n")

# 读取弹幕文本文件内容
def read_barrage_text():
    barrages = []
    with open('barrage_text.txt', 'r') as file:
        for line in file.readlines():
            barrages.append(line.strip())
    return barrages

# 初始化turtle屏幕
screen = t.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")  # 设置背景颜色为黑色
screen.tracer(0)  # 关闭自动更新，避免闪烁，后续手动更新

# 弹幕类
class Barrage:
    def __init__(self, text, x, y, speed, size, color):
        self.text = text
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color
        self.turtle = t.Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.color(self.color)
        self.turtle.write(self.text, align="left", font=("Arial", self.size, "normal"))

    def update(self):
        self.x -= self.speed  # 从右向左移动
        self.turtle.clear()
        self.turtle.goto(self.x, self.y)
        self.turtle.write(self.text, align="left", font=("Arial", self.size, "normal"))
        if self.x < -self.turtle.getscreen().window_width() / 2:  # 判断是否移出屏幕左侧，移出则从右侧重新进入
            self.x = SCREEN_WIDTH

    def draw(self):
        screen.update()  # 手动更新显示，避免闪烁


# 主函数
def main():
    create_barrage_text_file()  # 先创建弹幕文本文件
    barrages_text = read_barrage_text()
    barrages = []
    running = True
    while running:
        if len(barrages) < 10:
            text = r.choice(barrages_text)
            x = SCREEN_WIDTH
            y = r.randint(0, SCREEN_HEIGHT - BARRAGE_HEIGHT)
            speed = r.randint(BARRAGE_SPEED_MIN, BARRAGE_SPEED_MAX)
            size = r.randint(BARRAGE_SIZE_MIN, BARRAGE_SIZE_MAX)
            color = r.choice(TEXT_COLORS)
            new_barrage = Barrage(text, x, y, speed, size, color)
            barrages.append(new_barrage)

        for barrage in barrages:
            barrage.update()
            barrage.draw()

        time.sleep(0.05)

    t.done()


if __name__ == "__main__":
    main()

