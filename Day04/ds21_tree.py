import turtle as t
import random as r

angle = 30

def drawTree(length):
	if length < 10:
		return

	t.forward(length)
	
	t.right(angle)
	drawTree(length * 0.7)
	t.left(angle * 2)
	drawTree(length * 0.7)
	t.right(angle)

	t.backward(length)

t.speed(0)
t.penup()
t.setpos(0, -200)
t.pendown()
t.left(90)

drawTree(100)

t.done()