import turtle as t

class Pan(t.Turtle):#面向对象
    def __init__(self, n):
        """
        初始化盘子对象
        :param n: 盘子的宽度比例
        """
        super().__init__(shape='square', visible=False)
        self.up()
        self.sety(300)  # 初始位置在顶部
        self.shapesize(1, 2*n, 1)  # 设置盘子的宽度和高度
        self.fillcolor("green")  # 设置盘子的颜色
        self.showturtle()  # 显示盘子

class Peg(t.Turtle, list):
    def __init__(self, n, pos):
        """
        初始化柱子对象
        :param n: 柱子的高度比例
        :param pos: 柱子的x坐标位置
        """
        super().__init__(shape='square', visible=False)
        self.up()
        self.shapesize(n*1.5, .75, 2)  # 设置柱子的宽度和高度
        self.sety(10*n)  # 设置柱子的初始y坐标
        self.x = pos  # 柱子的x坐标
        self.setx(self.x)  # 设置柱子的x坐标
        self.showturtle()  # 显示柱子

    def push(self, disk):
        """
        将盘子放置在柱子上
        :param disk: 要放置的盘子对象
        """
        disk.setx(self.x)  # 设置盘子的x坐标与柱子相同
        disk.sety(10 + len(self) * 20)  # 设置盘子的y坐标，使其堆叠在柱子上
        self.append(disk)  # 将盘子添加到柱子的列表中

    def pop(self):
        """
        从柱子上移除盘子
        :return: 移除的盘子对象
        """
        disk = super().pop()  # 从柱子的列表中移除最上面的盘子
        disk.sety(300)  # 将盘子移动到顶部
        return disk

def move(from_peg, to_peg):
    """
    将盘子从一个柱子移动到另一个柱子
    :param from_peg: 起始柱子
    :param to_peg: 目标柱子
    """
    to_peg.push(from_peg.pop())

def hanoi(n, x, y, z):
    """
    汉诺塔递归函数
    :param n: 盘子的数量
    :param x: 起始柱子
    :param y: 目标柱子
    :param z: 辅助柱子
    """
    if n == 1:
        print(f"将盘子从 {x} 移动到 {y}")
        move(x, y)  # 将盘子从起始柱子移动到目标柱子
    else:
        # 将 n-1 个盘子从起始柱子移动到辅助柱子
        hanoi(n - 1, x, z, y)
        # 将第 n 个盘子从起始柱子移动到目标柱子
        print(f"将盘子从 {x} 移动到 {y}")
        move(x, y)
        # 将 n-1 个盘子从辅助柱子移动到目标柱子
        hanoi(n - 1, z, y, x)

def dh():
    """
    绘制底部的横线
    """
    t.pensize(15)
    t.penup()
    t.goto(-500, -10)
    t.pendown()
    t.goto(500, -10)

def main(n):
    """
    主函数，初始化并运行汉诺塔程序
    :param n: 盘子的数量
    """
    screen = t.Screen()
    pegs = [Peg(n, -200), Peg(n, 0), Peg(n, 200)]  # 创建三个柱子对象
    dh()  # 绘制底部的横线
    for i in range(n):
        pegs[0].push(Pan(n-i))  # 将盘子按顺序放置在第一个柱子上
    hanoi(n, *pegs)  # 使用新的汉诺塔函数
    #screen.bye()  # 关闭窗口

# 获取用户输入的盘子总数
n = int(input("请输入盘子总数："))
main(n)  # 运行主函数
    
                
        











