from turtle import *

size = 100
color = 'red'

fillcolor(color)
begin_fill()

for _ in range(6):
    forward(size)
    left(60)

end_fill()

exitonclick()