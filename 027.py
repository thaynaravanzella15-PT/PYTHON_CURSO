nome = str(input('Digite seu nome completo: ')).strip()
novo = nome.split()
print(f'Primeiro: {novo[0]}')
print(f'Último: {novo[len(novo) - 1]}')
