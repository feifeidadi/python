import turtle

t = turtle.Pen()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for x in range(1, 20):
    t.forward(100)
    t.left(95)

input("Press any key to continue")
