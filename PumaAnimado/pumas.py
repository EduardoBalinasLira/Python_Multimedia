# Animación Básica en Python 3
import turtle
import time

s = turtle.Screen()
s.bgcolor("navy")

# Se Registran las imágenes
turtle.register_shape("puma1.gif")
turtle.register_shape("puma2.gif")
turtle.register_shape("puma3.gif")
turtle.register_shape("puma4.gif")
turtle.register_shape("puma5.gif")
turtle.register_shape("puma6.gif")
turtle.register_shape("puma7.gif")
turtle.register_shape("puma8.gif")

p = turtle.Turtle()
ts = 0.04

while True:

	p.shape("puma1.gif")
	time.sleep(ts)
	p.shape("puma2.gif")
	time.sleep(ts)
	p.shape("puma3.gif")
	time.sleep(ts)
	p.shape("puma4.gif")
	time.sleep(ts)
	p.shape("puma5.gif")
	time.sleep(ts)
	p.shape("puma6.gif")
	time.sleep(ts)
	p.shape("puma7.gif")
	time.sleep(ts)
	p.shape("puma8.gif")
	time.sleep(ts)
wn.mainloop()

# Imágenes: https://docs.coronalabs.com/guide/media/spriteAnimation/index.html#image-sheets
