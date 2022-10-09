from turtle import *
hideturtle()

n = 250
if n > 200 and n < 260:
    pencolor('red')
if n > 100 and n < 200:
    pencolor('orange')
if n > 10 and n < 100:
    pencolor('yellow')

while n > 5:
    for i in range (5):

        circle(n, 90)
        left(90)
        circle(n, 90)
        left(18)
    n = n - 10






exitonclick()