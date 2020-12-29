import turtle
import time

#Cancha
wn = turtle.Screen()
wn.bgcolor("brown")
wn.setup(width=600, height=400)
wn.tracer(0)

#Pelota
pelota = turtle.Turtle()
pelota.hideturtle()
pelota.color("blue")
pelota.begin_fill()
pelota.circle(20)
pelota.end_fill()
pelota.penup()
pelota.goto(0,0)

#Variables para cambiar la velocidad de la pelota
vx = 3
vy = 3

while True:
    
    pelota.clear()

    pelota.penup()
    pelota.setx(pelota.xcor() + vx)
    pelota.sety(pelota.ycor() + vy)
    
    pelota.color("blue")
    
    pelota.begin_fill()
    pelota.circle(20)
    pelota.end_fill()

    if pelota.xcor() > 280:
      vx *= -1

    if pelota.ycor() > 160:
      vy *= -1

    if pelota.xcor() < -280:
      vx *= -1

    if pelota.ycor() < -200:
      vy *= -1

    time.sleep(.03)
    wn.update()
