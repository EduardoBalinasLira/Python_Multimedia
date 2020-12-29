import turtle
import time

s = turtle.Screen()
s.bgcolor("navy")

turtle.register_shape("zerox4_1.gif")
turtle.register_shape("zerox4_2.gif")
turtle.register_shape("zerox4_3.gif")
turtle.register_shape("zerox4_4.gif")
turtle.register_shape("zerox4_5.gif")
turtle.register_shape("zerox4_6.gif")
turtle.register_shape("zerox4_7.gif")
turtle.register_shape("zerox4_8.gif")
turtle.register_shape("zerox4_9.gif")
turtle.register_shape("zerox4_10.gif")
turtle.register_shape("zerox4_11.gif")
turtle.register_shape("zerox4_12.gif")

p = turtle.Turtle()
ts = 0.04

while True:

    p.shape("zerox4_1.gif")
    time.sleep(ts)
    p.shape("zerox4_2.gif")
    time.sleep(ts)
    p.shape("zerox4_3.gif")
    time.sleep(ts)
    p.shape("zerox4_4.gif")
    time.sleep(ts)
    p.shape("zerox4_5.gif")
    time.sleep(ts)
    p.shape("zerox4_6.gif")
    time.sleep(ts)
    p.shape("zerox4_7.gif")
    time.sleep(ts)
    p.shape("zerox4_8.gif")
    time.sleep(ts)
    p.shape("zerox4_9.gif")
    time.sleep(ts)
    p.shape("zerox4_10.gif")
    time.sleep(ts)
    p.shape("zerox4_11.gif")
    time.sleep(ts)
    p.shape("zerox4_12.gif")
    time.sleep(ts)
wm.mainloop()
