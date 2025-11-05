from datetime import date
ano_nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano_nasc
print(f'O atleta tem {idade} anos.')
if idade <=9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')