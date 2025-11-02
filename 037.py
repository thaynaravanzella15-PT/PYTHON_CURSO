#leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
cores = {'limpa':'\033[m','amarelo':'\033[32m','fverde':'\033[30;42m'}
n1 = int(input(f'{cores['amarelo']}Digite um número inteiro: {cores['limpa']}'))
print('Agora escolha qual será a quase de conversão')
conversao = int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\n Resp: '))
if conversao == 1:
    print('A conversão será em Binário')
    print(f'{cores['fverde']}{bin(n1)[2:]}{cores['limpa']}')
elif conversao == 2:
    print('A conversão será em Octal')
    print(f'{cores['fverde']}{oct(n1)[2:]}{cores['limpa']}')
else:
    print('A conversão será em Hexadecimal')
    print(f'{cores['fverde']}{hex(n1)[2:]}{cores['limpa']}')
