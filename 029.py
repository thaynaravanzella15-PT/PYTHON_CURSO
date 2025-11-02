from time import sleep
print('-=-'*20)
velocidade = float(input('Qual a velocidade do carro? [km/h] '))
print('-=-'*20)
if velocidade > 80:
    print('multado! você excedeu o limite permitido que é de 80km/h')
    print('O valor da multa será')
    print('PROCESSANDO...')
    sleep(2)
    valor = (velocidade - 80)*7
    print (f'R${valor:.2f} \nPrepare o bolso.')
print('Tenha um bom dia! Dirija com segurança!') #como é uma condição simples não precisei usar o else mas pode usar, vai dar certo igual. 
print('-=-'*20)