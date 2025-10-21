print('-'*30)
print('Conversor de valores')
print('-'*30)
dinheiro = float(input('Digite o valor que você tem em real: '))
dolares = float(input('Digite quanto esta o dolar atual: '))
conv = dinheiro/dolares
print(f'Você tem R${dinheiro} e na conversão atual são US${conv:.2f}')