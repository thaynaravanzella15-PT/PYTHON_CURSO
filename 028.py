from random import randint
from time import sleep #usa para o programa pensar um pouco, dar uma enrolada, eu escolho os segundos
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
computador = randint(0,5) #não precisa criar lista
print(f'O número escolhido foi {computador}')
if jogador == computador: #precisa lembrar que o simbolo para igual é sempre dois '=='
    print(f'Você acertou! eu pensei no {computador} ')
else:
    print(f'Você errou! eu pensei no {computador} ')


