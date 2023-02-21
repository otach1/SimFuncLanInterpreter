import math
import turtle
import turtle_CS
import numpy as np

turtle.setup(width=1.0,height=1.0)
turtle.penup()
turtle.speed(10)
turtle.delay(0)

turtle_CS.draw_cs()

for T in np.arange(1, 84, 1):
    x = T*2
    y = -math.log(T)*20
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 8, 0.1):
    x = T*20
    y = -math.exp(T)*0.1
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 300, 1):
    x = T*2
    y = 0*1
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 300, 1):
    x = 0*2
    y = -T*1
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 120, 1):
    x = T*2
    y = -T*1
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 55, 1):
    x = T*2
    y = -(T*T)*0.1
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 60, 1):
    x = T*10
    y = -math.sqrt(T)*5
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

for T in np.arange(0, 60, 0.01):
    x = math.cos(T)*100
    y = -math.sin(T)*50
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot-300,y_rot+300)
    turtle.dot()

turtle.done()