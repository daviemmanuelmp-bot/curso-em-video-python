s1 = float(input('Qual é o salário do funcionário? R$'))
if s1 <= 1250:
    print('Você teve um aumento de 15%, seu novo salário é R${:.2f}'.format(s1 * 1.15))
else:
    print('Você teve um aumento de 10%, seu novo salário é R%{:.2f}'.format(s1 * 1.1))
