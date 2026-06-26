s1 = float(input('Qual é o salário do funcionário? R$'))
d1 = float(input('Qual a porcentagem do aumento? '))
print('O novo salário com {}% de aumento é R${:.2f}'.format(d1, s1 * ((d1 + 100) / 100)))
