import turtle
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(0)

def circle(distance, color):
    bob.circle(distance)
    bob.color(color)

def spiral():
    bob.shape("turtle")
    for times in range(450):
        bob.color(times, times, times)
        bob.forward(times * 2)
        bob.left(122)

def spiral2(distance):
    bob.shape("turtle")
    for times in range(20):
        c = times * 15
        bob.color(c,c,c)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 45)

def spikeFlower(distance):
    for times in range(11):
        c = times * 20
        bob.color(c,c,c)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 36)


def spike(distance):
    for times in range(20):
        c = times * 12
        bob.color(c,c,c)
        bob.width(times * 2)
        bob.forward(distance)
        bob.left(10)
        
        
def tile(c):
    polygon(4, 200, c )
    for times in range(4):
        polygon(3, 50, "black")
        bob.forward(50)
        polygon(3, 50, "black")
        bob.forward(50)
        polygon(3, 50, "black")
        bob.forward(50)
        polygon(3, 50, "black")
        bob.forward(50)
        bob.left(90)

def rowtile(c):
    for times in range(8):
        tile(c)
        bob.forward(200)

def square(distance):
    for times in range(4):
        bob.forward(distance)
        bob.left(90)

def triangle(distance):
    for times in range(3):
        bob.forward(distance)
        bob.left(120)

def pentagon(distance):
    sides = 5
    angle = 360 / sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

def polygon(sides, distance, c):
    bob.color( c )
    angle = 360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def figure1(distance, size, color):
    bob.color( color )
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(100)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()

def monster(size, color):
    bob.begin_fill()
    bob.color(color)
    bob.left(90)
    bob.forward(100)
    bob.circle(size)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.left(45)
    bob.forward(24)
    bob.right(90)
    bob.forward(24)
    bob.left(45)
    bob.left(45)
    bob.forward(24)
    bob.right(90)
    bob.forward(24)
    bob.left(45)
    bob.left(45)
    bob.forward(24)
    bob.right(90)
    bob.forward(24)
    bob.left(45)
    bob.end_fill()

def fadingTriangle():
    for times in range(50):
        c = (250 - times *5, 250 - times * 5, 0)
        polygon(10, 450 - times * 8, c )
    
