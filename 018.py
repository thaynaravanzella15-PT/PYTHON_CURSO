from math import radians, sin, cos, tan
ângulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ângulo))
coss = cos(radians(ângulo))
tang = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem\nseno: {seno:.2f} \ncosseno: {coss:.2f} \ntangente: {tang:.2f}')

