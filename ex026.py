frase = str(input('Digite uma frase: ')).upper()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "a" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))
