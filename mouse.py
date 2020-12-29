import turtle
import random

t = turtle.Turtle()
t.shape('turtle')
t.color('brown')

s = turtle.Screen()


t.stamp()

colores1 = ['brown']

colores = ["green", "forest green", "dark green", "yellow green", "olive drab", "sea green", "medium sea green", "dark sea green", "olive", "dark olive green", "light sea green"]

def clic(x,y):
  
  t.color(random.choice(colores))
  t.goto(x,y)
  t.shapesize(random.randint(1,5))
  t.stamp()



def clicD(x,y):
    t.color(random.choice(colores1))
    t.goto(x,y)
    t.shapesize(random.randint(1,5))
    t.left(180)
    t.stamp()
    t.left(180)
        

s.onclick(clic,1)
s.onclick(clicD,3)

