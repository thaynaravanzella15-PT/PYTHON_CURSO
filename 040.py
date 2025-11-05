#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a 1°Nota: '))
nota2 = float(input('Digite a 2°Nota:'))
media = (nota1 + nota2)/2
if media < 5:
    print(f'A sua média foi {media:.1f} e você está \033[31mReprovado\033[m')
elif media >= 5 and media <= 6.9:
    print(f'A sua média foi {media:.1f} e você está em \033[33mRecuperação\033[m')
elif media >= 7:
    print(f'A sua média foi {media:.1f} e você está \033[32mAprovado\033[m')