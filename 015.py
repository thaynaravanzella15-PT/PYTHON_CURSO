km=float(input('Quantos km você percorreu com o carro? '))
dia=int(input('Por quantos dias você usou o carro? '))
preco = (km*0.15)+(dia*60)
print(f'Esse aluguel teve um custo total de R${preco:.2f}')
