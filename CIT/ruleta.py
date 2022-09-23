import random

print ("VÍTEJTE NA FRANCOUZSKÉ RULETĚ")
print ("Zkuste své štěstí!")
tip = input ("Tipujte které čílo padne na ruletě: ")
tip = int(tip)
if (tip % 2) == 0 and (tip >=1 and tip<=10) or (tip>=19 and tip<= 28): 
    print (tip, " je černá sudá")
elif (tip % 2) == 1 and  (tip >=1 and tip<=10) or (tip>=19 and tip<= 28): 
    print (tip, " je červená lichá")
elif (tip % 2) == 1 and  (tip >=11 and tip<=18) or (tip>=29 and tip<= 36): 
    print (tip, " je černá lichá")
elif (tip % 2) == 0 and  (tip >=1 and tip<=10) or (tip>=19 and tip<= 28): 
    print (tip, " je červená lichá")
else:
    print ("tvůj tip je zelená nula")

padlo = random.randint(0,36)
if padlo == tip:
    print ("váš tip vyhrává!")
else:
    print("tipovali jste", tip, "ale padlo", padlo )
    print ("váš tip nevyhrává :( ")
    