from turtle import *
from random import *
from time import *

#Особые фигуры

# Важно! Переменная col должна задаваться как строка (например, "red"), а переменная fill должна иметь значение 1, если вы хотите заливку.

def star(scale, fill, col):
    color(col)
    if fill == 1:
        begin_fill()
    for i in range(5):
        left(144)
        forward(scale)
    if fill == 1:
        end_fill()
    setheading(0)

def eight(scale, fill, col):
    color(col)
    if fill == 1:
        begin_fill()
    for i in range(8):
        left(45)
        forward(scale)
    if fill == 1:
        end_fill()
    setheading(0)

def rhomb(scale, fill, col):
    color(col)
    left(45)
    if fill == 1:
        begin_fill()
    for i in range(4):
        left(90)
        forward(scale)
    if fill == 1:
        end_fill()
    setheading(0)

def square(scale, fill, col):
    color(col)
    if fill == 1:
        begin_fill()
    for i in range(4):
        left(90)
        forward(scale)
    if fill == 1:
        end_fill()
    setheading(0)
    

#Функции

def remove():
    penup()
    color("white")
    goto(-250, -250)
    pendown()

    begin_fill()

    for i in range(4):
        forward(1000)
        left(90)

    end_fill()

def gotoL(posX, posY):
    penup()
    goto(posX, posY)
    pendown()

#Ассеты

def ground():
    penup()
    color("green")
    goto(-250, -275)
    pendown()

    begin_fill()

    for i in range(4):
        forward(250)
        left(90)

    penup()
    goto(0, -275)
    pendown()

    for i in range(4):
        forward(250)
        left(90)

    color("green")
    
    end_fill()
    setheading(0)

def middle_ground():
    penup()
    color("grey")
    goto(-250, -335)
    pendown()

    begin_fill()

    for i in range(4):
        forward(250)
        left(90)

    end_fill()

    begin_fill()

    penup()
    color("grey")
    goto(0, -335)
    pendown()

    for i in range(4):
        forward(250)
        left(90)

    color("grey")
    
    end_fill()

    penup()
    color("black")
    goto(-250, -365)
    pendown()

    begin_fill()

    for i in range(4):
        forward(250)
        left(90)

    end_fill()

    begin_fill()

    penup()
    color("black")
    goto(0, -365)
    pendown()

    for i in range(4):
        forward(250)
        left(90)

    color("black")
    
    end_fill()
    setheading(0)

def sun(col):

    color(col)

    begin_fill()

    for i in range(23):
        forward(70)
        left(105)

    end_fill()

def particles(col, repeats):
    for i in range(repeats):
        begin_fill()
        color(col)
        circle(randint(5, 20))
        penup()
        left(randint(-180, 180))
        forward(randint(10, 70))
        end_fill()

def mountains(posX, posY):
    penup()
    goto(posX, posY)
    pendown()
    pensize(10)

    for i in range(4):  
        color("indigo")
        left(70)
        forward(50)
        right(140)
        forward(50)
        left(140)
        color("thistle")
        forward(100)
        right(140)
        forward(100)
        left(70)

def spiral(posX, posY, repeats, col):
    color(col)
    gotoL(posX, posY)
    scale = 10

    pensize(3)
    speed(10)

    for i in range(repeats):
        forward(scale)
        left(90)
        scale += 10

def up(repeats, size, col, posX, posY):
    pensize(size)
    gotoL(posX, posY)
    color(col)

    for i in range(repeats):
        forward(30)
        left(90)
        forward(30)
        right(90)

#Примеры

def Turtle_run():
    x = -200

    color("grey")
    left(270)
    for i in range(10):
        penup()
        speed(50)
        goto(x, 1000)
        pendown()
        forward(1250)
        x += 45

    t1 = Turtle()
    t1.color("blue")
    t1.shape("turtle")
    t1.penup()
    t1.goto(-200, 100)
    t1.pendown()

    t2 = Turtle()
    t2.color("red")
    t2.shape("turtle")
    t2.penup()
    t2.goto(-200, -100)
    t2.pendown()

    t1.speed = int(input("Средняя скорость 1 черепахи:"))
    t1.speed2 = int(input("Максимальная скорость 1 черепахи:"))

    t2.speed = int(input("Средняя скорость 2 черепахи:"))
    t2.speed2 = int(input("Максимальная скорость 2 черепахи:"))

    finish = int(input("Финиш:"))

    while t1.xcor() < finish and t2.xcor() < finish:
        if t1.speed <= t1.speed2:
            t1.forward(randint(t1.speed, t1.speed2))
        else:
            t1.forward(randint(t1.speed2, t1.speed))
        
        if t2.speed <= t2.speed2:
            t2.forward(randint(t2.speed, t2.speed2))
        else:
            t2.forward(randint(t2.speed2, t2.speed))

    if t1.xcor() >= finish:
        t1.left(360)
    else:
        t2.left(360)