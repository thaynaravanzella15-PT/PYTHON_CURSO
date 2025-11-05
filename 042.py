r1 = int(input('Primeira reta '))
r2 = int(input('Segunda reta '))
r3 = int(input('Terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM formar um triângulo', end='') #O END é para seguir no proximo print na mesma frase.
    if r1 == r2 and r2 == r3:  # ou pode escrever r1 == r2 == r3
       print(' EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('As retas acima NÃO PODEM formar triângulo')