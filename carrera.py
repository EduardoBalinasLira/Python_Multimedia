import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.penup()

#Tortuga roja
t_roja = turtle.Turtle()
t_roja.color("red")
t_roja.shape('turtle')

t_roja.penup()
t_roja.goto(0,20)
t_roja.pendown()

t_azul = turtle.Turtle()
t_azul.color("blue")
t_azul.shape('turtle')

t_azul.penup()
t_azul.goto(10,40)
t_azul.pendown()


t_verde = turtle.Turtle()
t_verde.color("green")
t_verde.shape('turtle')

t_verde.penup()
t_verde.goto(20,60)
t_verde.pendown()

for primera in range(150):
    t_roja.forward(random.randint(1,4))
    t_azul.forward(random.randint(1,4))
    t_verde.forward(random.randint(1,4))

t_roja.left(90)
t_azul.left(90)
t_verde.left(90)


for segunda in range(60):
    
    t_roja.forward(random.randint(1,4))
    t_azul.forward(random.randint(1,4))
    t_verde.forward(random.randint(1,4))

t_roja.left(90)
t_azul.left(90)
t_verde.left(90)

for tercera in range(150):
    
    t_roja.forward(random.randint(1,4))
    t_azul.forward(random.randint(1,4))
    t_verde.forward(random.randint(1,4))



t_roja.left(90)
t_azul.left(90)
t_verde.left(90)

for i in range(60):
    t_roja.forward(random.randint(1,4))
    t_azul.forward(random.randint(1,4))
    t_verde.forward(random.randint(1,4))

t_roja.write("Hola")
    
print(t_roja.pos())
print(t_azul.pos())
print(t_verde.pos())

t_roja.goto(0,20)
t_verde.goto(20,60)
t_azul.goto(10,40)







