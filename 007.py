print('='*20)
print('B O L E T I M')
print('='*20)
nome=input('Qual o nome do aluno: ')
n1=float(input('Digite a nota 1 do {}: '.format(nome)))
n2=float(input('Digite a nota 2 do {}: '.format(nome)))
media=(n1+n2)/2
print('A média do {} é {:.1}'.format(nome,media))
