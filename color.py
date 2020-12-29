import colorsys
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.pensize(180)
t.speed(10)

hue = 0.0
s = 0.0
v = 0.0
i = 0
while True:
    
    t.color(colorsys.hsv_to_rgb(hue,1,1))
    t.fd(2)
    t.left(1)
    
    hue += 0.0027
    i += 1
    if i >= 360:
        break
