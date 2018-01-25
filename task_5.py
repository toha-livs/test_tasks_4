slovo = 'The-Phantom_Menace'
cou = slovo.count('_') + slovo.count('-')
slovo = slovo.replace('-', ' ', cou)
slovo = slovo.replace('_', ' ', cou)
slovo_1 = slovo[0]
slovo = slovo.title()
slovo = slovo.replace(' ', '', cou)
print(slovo_1 + slovo[1:])
