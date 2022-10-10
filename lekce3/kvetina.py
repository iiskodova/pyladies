from turtle import *
hideturtle()

n = 250
pencolor('red4')

while n > 5:
    for i in range (5):

        circle(n, 90)
        left(90)
        circle(n, 90)
        left(18)
            
    n = n - 10

    if n > 240 :
        pencolor('red3')
    if n > 200 and n < 240:
        pencolor('red1')
    if n > 160 and n < 200:
        pencolor('orange3')
    if n > 120 and n < 160:
        pencolor('orange1')
    if n > 80 and n < 120:
        pencolor('DarkGoldenrod3')
    if n > 40 and n < 80:
        pencolor('DarkGoldenrod1')
    if n > 40 and n < 0:
        pencolor('goldenrod1')
