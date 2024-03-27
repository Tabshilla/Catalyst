import turtle
tr=turtle.Turtle()
tr.pensize(5)
def color1(cl1):
    tr.color("blue")
    tr.penup()
    tr.goto(-110,-25)
    tr.pendown()
    tr.circle(45)


def color2(cl2):
    tr.color("black")
    tr.penup()
    tr.goto(0,-25)
    tr.pendown()
    tr.circle(45)


def color3(cl3):
    tr.color("red")
    tr.penup()
    tr.goto(110,-25)
    tr.pendown()
    tr.circle(45)

def color4(cl4):
    tr.color("yellow")
    tr.penup()
    tr.goto(-55,-75)
    tr.pendown()
    tr.circle(45)
    tr.penup()

def color5(cl5):
    tr.color("green")
    tr.penup()
    tr.goto(55,-75)
    tr.pendown()
    tr.circle(45)
    tr.penup()


def logo():
    color1("blue")
    color2("black")
    color3("red")
    color4("yellow")
    color5("green")
logo()