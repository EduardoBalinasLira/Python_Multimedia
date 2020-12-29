import turtle

t = turtle.Turtle()
t.shape("turtle")

#Esquinas

x = 40
y = 200
#/Esquinas

#Color

t.color("green")

#/Color

while y > 80:
    t.penup()
    t.goto(0,y)
    t.pendown()

    t.goto(x,0)
    y -= 20
    x += 20

x = 140
y = 80
xy = 20

while y >= 0:
    t.penup()
    t.goto(0,y)
    t.pendown()
    

    t.goto(x,xy)
    y -= 20
    xy += 20

x = 40
y = 120

while x <= 140 and y <= 200:
    t.penup()
    t.goto(x,0)
    t.pendown()

    t.goto(140, y)
    y += 20
    x += 20



    
    
