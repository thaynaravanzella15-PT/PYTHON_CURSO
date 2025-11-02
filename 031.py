distancia = int(input('Qual é a distancia da sua viagem? '))
if distancia <= 200:
    distancia = distancia * 0.50
    print(f'O valor da viagem será de R${distancia:.2f}')
else:
    distancia = distancia * 0.45
    print(f'O valor da viagem será de R${distancia:.2f}')
print('==Tenha uma boa viagem==')
#é possivel fazer de uma forma simplificada mas ai vai de pessoa para pessoa como por exemplo
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(preco)