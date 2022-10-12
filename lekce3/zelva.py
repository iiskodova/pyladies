from turtle import circle, fillcolor, pencolor, pendown, penup, right, left, forward, shape, exitonclick, speed
shape('turtle')
pencolor('red')
speed('slow')

#podtržítko místo proměnné kterou tady nepotřebuji 
penup()
left(180)
forward(400)
right(180)
for i in range(0, 18): # proměnná i je to, co chci zvětšovat(cyklit) range je rozmezí čísel o které se to vždy zvětší, 0, 1, 2, 3...
   
    pendown()
    forward(i * 10)
    penup()
    forward(50)
    
    
 
exitonclick()