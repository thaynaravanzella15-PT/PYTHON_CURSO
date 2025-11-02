cores = {'limpa':'\033[m','azul':'\033[34m','roxo':'\033[35m','pretoebranco':'\033[40;35m'}
print(f'{cores['pretoebranco']}*{cores['limpa']}'*35)
print(f'{cores['roxo']} FINANCIAMENTO DA SUA TENDA{cores['limpa']}')
print(f'{cores['pretoebranco']}*{cores["limpa"]}'*35)
tenda = float(input('Qual o valor da tenda? R$'))
sal = float(input('Indique seu salario? R$'))
tempo = int(input('Em quantos anos pretende pagar?'))
mes = tempo * 12
emprestimo = tenda/mes
nsal= sal*0.30
if emprestimo >= nsal:
    print(f'{cores['azul']}PARABÉNS!! agora você tem uma tenda e uma divida{cores['limpa']}')
else:
    print(f'\033[31mVixi deu errado, quem sabe em mais prestações?{cores['limpa']}')