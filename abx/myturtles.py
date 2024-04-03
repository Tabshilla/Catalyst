import turtle
tr=turtle.Turtle()
tr.pensize(5)

tr.color("black")
tr.left(90)
tr.backward(100)
tr.speed(100)
tr.shape('turtle')

def tree(i):
    if i < 10:
        return 
    else:
        tr.forward(i)
        tr.color("green")
        tr.circle(2)
        tr.color("blue")
        tr.left(30)
        tree(3*i/4)
        tr.right(60)
        tree(3*i/4)
        tr.left(30)
        tr.backward(i)
tree(100)
turtle.done()