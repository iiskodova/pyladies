dictionary = {
    'Gwynbleidd': 'wolf', 
    'Angharad': 'raven', 
    'Sian': 'octopus', 
    'Meru': 'squirrel'
    }

for k, v in dictionary.items():
    print(k + ' is a ' + v)
print()

dictionary['Gwynbleidd'] = 'white wolf'

for k, v in dictionary.items():
    print(k + ' is a ' + v)
print()

dictionary['Edgar'] = 'jackal'

for k, v in dictionary.items():
    print(k + ' is a ' + v)
print()

del dictionary['Angharad']

for k, v in dictionary.items():
    print(k + ' is a ' + v)