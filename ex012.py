n1 = float(input('Qual o preço do produto? R$'))
d1 = float(input('Qual a porcentagem do desconto? '))
print('O novo preço com {}% de desconto é R${:.2f}!'.format(d1, n1 * ((100 - d1) / 100)))