import turtle

t = turtle.Turtle()

t.left(90)

def tree(i):
    if i < 10:
        print("hola")
    else:
        t.fd(i)
        t.left(30)
        tree(3 * i / 4)
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        t.backward(i)
tree(50)
