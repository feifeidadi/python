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
for x in range(1, 38):
    t.forward(100)
    t.left(175)

input("Press any key to continue")

