from turtle import *
hideturtle()

n = 250
pencolor('darkslategrey')

while n > 5:
    for i in range (5):
        circle(n, 90)
        left(90)
        circle(n, 90)
        left(18)
            
    n = n - 10

    if n > 240 :
        pencolor('darkcyan')
    if n > 200 and n < 240:
        pencolor('cyan4')
    if n > 160 and n < 200:
        pencolor('lightseagreen')
    if n > 120 and n < 160:
        pencolor('cyan3')
    if n > 80 and n < 120:
        pencolor('cyan2')
    if n > 40 and n < 80:
        pencolor('aquamarine1')
    if n > 40 and n < 0:
        pencolor('darkslategray1')

exitonclick()
