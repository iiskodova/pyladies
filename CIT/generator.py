import random
prvni = input("zadej spodní hranici: ")
druha = input("zadej horní hranici: ")
prvni = int(prvni)
druha = int(druha)
výsledek = random.randint(prvni,druha)
print ("vylosoval jsi dodatkové číslo", výsledek)