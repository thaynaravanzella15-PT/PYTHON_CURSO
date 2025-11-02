r1 = int(input('Primeira reta '))
r2 = int(input('Segunda reta '))
r3 = int(input('Terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM formar triangulo')
else:
    print('As retas acima NÃO PODEM formar triangulo')