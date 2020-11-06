import turtle
from math import sqrt

loops = 0
x = 45
y = 0

turtle.shape('turtle')
dlina = 30
null = [0, 180, 90, 0, 90, 90, 0]
one = [45, -135, 0, 180, 0]
two = [0, -90, -45, 135, 180, -135, 45]
three = [0, -135, 135, -135]
four = [-135, 90, -89, 180, 0]
five = [0, 180, 90, 90, -90, -90]
six = []
seven = [0, -135, 45]
chisla = [null, one, two, three, four, five]
for row in chisla:
    if row == one or six:
        turtle.penup()
        turtle.left(-90)
        turtle.forward(dlina)
        turtle.left(90)
        turtle.pendown()
    """elif row == three:
        turtle.penup()
        turtle.left(90)
        turtle.forward(dlina*2)
        turtle.pendown()
    """
    for elem in row:

        turtle.left(elem)
        if (row == one and elem == 45) or (row == two and (elem == -45 or elem == -135)) \
                or (row == three and (elem == -135)):
            turtle.forward(sqrt(dlina**2 + dlina**2))

        else:
            turtle.forward(dlina)

    turtle.right(90)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x += 45









turtle.mainloop()
