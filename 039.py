#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano_nasc = int(input('Em que ano você nasceu? '))
ano_atual = datetime.date.today().year - ano_nasc
if ano_atual <18:
    print(f'\033[33mAinda não é hora de se alistar! falta {18-ano_atual} anos para o alistamento.\033[m')
elif ano_atual == 18:
    print('\033[32mPrecisa se alistar esse ANO!\033[m')
else:
    print('\033[31mJá passou o ano do alistamento\033[m')