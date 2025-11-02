import math
cateto =float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(cateto,adjacente)
print(f'O comprimento de hipotenusa é {hipotenusa:.3}')
print('-'*30)
