from parser import MyParser
import math
import turtle
import turtle_CS
import numpy as np


class Interpreter:
    def __init__(self, path):
        self.MidCode = MyParser.Parser(path).analyze()
        # 初始化画布
        turtle.setup(width=1.0, height=1.0)
        turtle.penup()
        turtle.speed(10)
        turtle.delay(0)
        turtle_CS.draw_cs()

    def create(self):
        # 解析中间代码
        for i in self.MidCode:
            # 操作每一次画图
            for T in np.arange(i[3][0], i[3][1], i[3][2]):
                x = eval(i[4][0])*i[1][0]
                y = eval(i[4][1])*i[1][1]
                x_rot = x * math.cos(i[2])+y*math.sin(i[2])+i[0][0]
                y_rot = y * math.cos(i[2])-x*math.sin(i[2])+i[0][1]
                turtle.goto(x_rot-300, y_rot+300)
                turtle.dot()
        turtle.done()
