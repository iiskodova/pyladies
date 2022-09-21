strana = float(input('zadej číslo: '))
cislo_je_spravne = strana > 0 
if cislo_je_spravne:
    print('obsah čtverce se stranou', strana, 'je', 4 * strana, 'cm')
else: 
    print('strana musí být větší než nula!')
print('děkujeme za použití geometrické kalkulačky')
