import turtle
from math import sqrt
loops = 0
x = 45
y = 0
turtle.shape('turtle')
dlina = 30
zero = [0, 180, 90, 0, 90, 90, 0]
one = [45, -135, 0, 180, 0]
two = [0, -90, -45, 135]
three = [0, -135, 135, -135]
four = [-90, 90, -90, 180, 0]
five = [0, 180, 90, 90, -90, -90]
six = [-90, 90, 90, 90, -135 ]
seven = [0, -135, 45]
eight = [0, -90, 0, -90, -90, -90, 180, -90, -90]
nine = [0, -90, -90, -90, -90, -90, -45]
chisla = [zero, one, two, three, four, five, six, seven, eight, nine]
for row in chisla:
    if row == one or row == six:
        turtle.penup()
        turtle.left(-90)
        turtle.forward(dlina)
        turtle.left(90)
        turtle.pendown()
    for elem in row:
        turtle.left(elem)
        if (row == one and elem == 45) or (row == two and (elem == -45 or elem == -135)) \
                or (row == three and (elem == -135)) or (row == six and (elem == -135)) \
                or (row == seven and (elem == -135)) or (row == nine and elem == -45):
            turtle.forward(sqrt(dlina**2 + dlina**2))
        else:
            turtle.forward(dlina)
    turtle.setheading(90)
    turtle.right(90)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x += 45









turtle.mainloop()
