#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano_nasc
if idade <18:
    saldo = 18 - idade
    ano = date.today().year + saldo
    print(f'\033[33mAinda não é hora de se alistar! falta {18 - idade} anos para o alistamento.\033[m')
    print(f'Será em {ano}')
elif idade == 18:
    print(f'Você tem {idade} anos em {date.today().year}')
    print('\033[32mPrecisa se alistar esse ANO!\033[m')
else:
    saldo = idade - 18
    print(f'Você tem {idade} anos em {date.today().year}')
    print(f'\033[31mJá passou o ano do alistamento\033[m')
    print(f'Seu alistamento foi em {date.today().year - saldo}')