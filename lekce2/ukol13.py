print('Ahoj, vítáme tě v našem obchůdku!')
print('Kolik máš u sebe peněz?')
peníze = int(input('Mám u sebe 1-1000 zlaťáků: '))


if peníze == 0:
    print('tak to nás mrzí, ale zadarmo ti nic nedáme. zkus přijít jindy.')
if peníze >= 1 and peníze <= 10: 
    print('pro tebe máme na výběr čokoládové žabky nebo bertíkovy fazolky!')
elif peníze >=11 and peníze <=100:
    print('můžeš si u nás vybrat z těchto devíti prstenů!')
elif peníze >=101 and peníze <=299: 
    print('ty máš dost peněz na amulet, chceš vlka, kočku, nebo medvěda?')
elif peníze >=300 and peníze <=699:
    print('tebe by mohly zajímat tyhle fremenské věci...')
elif peníze >=700 and peníze <=899:
    print('mohla bych ti nabídnout některý z našich plášťů neviditelnosti?')
elif peníze >=900 and peníze <=1000:
    print('mám tu pro tebe jednu vzácnou věcičku, hned pro ni dojdu...')
elif peníze >=1001 and peníze <=99999:
    print('ty jsi opravdový boháč a jistě víš, pro co jsi přišel. tobě nemusím nic nabízet, povídej, co bys rád?')
elif peníze >=100000:
    print('hohó, ty si můžeš koupit celý obchod!')
else:
    print('šprýmaře jako ty tu nevidíme rádi!')
