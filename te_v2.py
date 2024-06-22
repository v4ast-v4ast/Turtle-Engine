from turtle import *
from random import *
from time import *

def error01():
    while True:
        print("Ошибка: переменная fill должна быть равна 0 или 1")

def error02():
    while True:
        print("Ошибка: переменная gradus должна быть меньше 281 и больше 259")

def error03():
    while True:
        print("Ошибка: переменная rev должна быть равна 0 или 1")

#Особые фигуры

# Важно! Переменная col должна задаваться как строка (например, "red"), а переменная fill должна иметь значение 1, если вы хотите заливку.

def star(scale, fill, col):
    color(col)
    if fill != 0 and fill != 1:
        error01()
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
    if fill != 0 and fill != 1:
        error01()
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
    if fill != 0 and fill != 1:
        error01()
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
    if fill != 0 and fill != 1:
        error01()
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

def spiral(posX, posY, repeats, col, rev):
    color(col)
    gotoL(posX, posY)
    scale = 10

    pensize(3)
    speed(10)

    if rev != 0 and rev != 1:
        error03()

    if rev == 0:
        for i in range(repeats):
            forward(scale)
            left(90)
            scale += 10
    else:
        for i in range(repeats):
            forward(scale)
            right(90)
            scale += 10


def up(repeats, size, col, posX, posY, rev):
    pensize(size)
    gotoL(posX, posY)
    color(col)

    if rev != 0 and rev != 1:
        error03()

    for i in range(repeats):
        forward(30)
        if rev == 0:
            left(90)
        elif rev == 1:
            right(90)
        forward(30)
        if rev == 0:
            right(90)
        elif rev == 1:
            left(90)

def rays(size, gradus, col, repeats, posX, change):
    pensize(size)
    color(col)

    if gradus > 280 or gradus < 260:
        error02()

    for i in range(repeats):
        if gradus >= 260 or gradus <= 280:
            setheading(gradus)
        else:
            setheading(randint(260, 280))
        gotoL(posX, 400)
        forward(800)
        gradus += change

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

def Simple_paint():
    hideturtle()
    print("Инструкция:")
    print("Цифры от 1 до 4 - изменить размер")
    print("Буквы R, G, B, Y, D - цвета")
    print("Буква W - стерка")
    print("Буквы Z, X, C - скорость")
    print("Зажатие цифры 5 - рисование ИИ")
    print("Буквы F, D - начать/закончить заливку")


    t = Turtle()
    scr = t.getscreen()
    print("Выберите форму:")
    print("[1] - круг")
    print("[2] - треугольник")
    print("[3] - квадрат")
    print("[4] - черепашка")
    shape = input()

    def draw(x, y):
        t.goto(x, y)

    def move(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    t.speed(50)

    if shape == "1":
        t.shape("circle")
    if shape == "2":
        t.shape("triangle")
    if shape == "3":
        t.shape("square")
    if shape == "4":
        t.shape("turtle")
    else:
        t.shape("circle")

    t.ondrag(draw)
    scr.onscreenclick(move)
    t.save_pensize = 0

    def setRed():
        t.color("red")

    def setGreen():
        t.color("green")
    
    def setBlue():
        t.color("blue")
    
    def setYellow():
        t.color("yellow")

    def setBlack():
        t.color("black")

    def setWhite():
        t.color("white")

    def size1():
        t.pensize(2)
        save_pensize = 2
    
    def size2():
        t.pensize(5)
        save_pensize = 5

    def size3():
        t.pensize(10)
        save_pensize = 10
    
    def size4():
        t.pensize(25)
        save_pensize = 25

    def speed1():
        t.speed(15)

    def speed2():
        t.speed(30)

    def speed3():
        t.speed(50)

    def ai_draw():
        t.forward(randint(-10, 10))
        t.left(randint(-10, 10))
        if randint(0, 5) == 0:
            t.color("red")
        if randint(0, 5) == 1:
            t.color("green")
        if randint(0, 5) == 2:
            t.color("blue")
        if randint(0, 5) == 3:
            t.color("yellow")
        if randint(0, 5) == 4:
            t.color("black")
        if randint(0, 5) == 5:
            t.color("white")

    def begin_f():
        t.begin_fill()

    def end_f():
        t.end_fill()

    scr.listen()
    scr.onkey(setRed, "r")
    scr.onkey(setGreen, "g")
    scr.onkey(setBlue, "b")
    scr.onkey(setYellow, "y")
    scr.onkey(setBlack, "d")
    scr.onkey(setWhite, "w")
    scr.onkey(size1, "1")
    scr.onkey(size2, "2")
    scr.onkey(size3, "3")
    scr.onkey(size4, "4")
    scr.onkey(speed1, "z")
    scr.onkey(speed2, "x")
    scr.onkey(speed3, "c")
    scr.onkey(ai_draw, "5")
    scr.onkey(begin_f, "f")
    scr.onkey(end_f, "d")
            
speed(0)
Simple_paint()
exitonclick()