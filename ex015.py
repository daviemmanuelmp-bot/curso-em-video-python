d = float(input('Quantos dias alugados? '))
r = float(input('Quantos km rodados? '))
print('O total a pagar é R${:.2f}'.format((d * 60) + (r * 0.15)))