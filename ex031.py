p1 = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(p1))
if p1 <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(p1 * 0.5))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(p1 * 0.45))

