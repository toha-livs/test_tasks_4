f = []
spisok = [{'name': 'John'}, {'name': 'Jack'}]
if len(spisok) == 1:
    print(spisok[0]['name'])
elif len(spisok) == 2:
    names_1 = [i['name'] for i in spisok]
    last_name = names_1.pop()
    first_name = names_1.pop()
    print(first_name + ' & ' + last_name)
else:
    names_1 = [i['name'] for i in spisok]
    last_name = names_1.pop()
    penult_name = names_1.pop()
    for i in names_1:
        print(i, end=', ')
    print(penult_name + ' & ' + last_name)
