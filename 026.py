frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra a: {(frase.count('A'))}')
print(f'Qual a primeira posição que aparece? {frase.find('A')+1}')
print(f'Qual a ultima posição que aparece? {frase.rfind('A')+1}')