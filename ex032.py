from datetime import date
a1 = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a1 == 0:
    a1 = date.today().year
if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0:
    print('O ano {} é BISSEXTO!!'.format(a1))
else:
    print('O ano {} NÃO é BISSEXTO'.format(a1))