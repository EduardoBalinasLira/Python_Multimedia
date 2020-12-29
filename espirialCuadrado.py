import turtle
import random

t = turtle.Turtle()
t.shape("turtle")


#colores = ["red","green","orange","Violet"]

def cuadrado():
    for i in range(1,100):
        t.fd(100 + i*2)
        t.left(90 + i)

cuadrado()


#def cuadrado(a):
#    for i in range(4):
#        t.fd(a)
#        t.left(90)

#for i in range(10):
#    for j in range(10):
#        r = random.randint(0,4)
#        cuadrado()
#        t.fd(10)
#        t.left(5)
#        t.color(colores[r])
    
#for i in range(360):
#    cuadrado(i * 2)
#    t.left(5)

