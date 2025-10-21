print('-'*30)
print('Tabela de conversão')
print('-'*30)
metros=float(input('Digite o valor em metros que deseja converter '))
cm=metros*100
mm=metros*1000
print('{}m equivale a {:.0f}cm e {:.0f}mm'.format(metros,cm,mm))
print('-'*30)
#ou
print(f'{metros}m equivale a {cm:.0f}cm e {mm:.0f}mm')
#:.0f significa sem casa decimais