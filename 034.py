sal = float(input('Salário do funcionário R$'))
if sal <= 1250:
    novo = sal + (sal * 0.15)
else:
    novo = sal + (sal * 0.10)
print(f'O novo salário é \33[1;33mR${novo}\33[m')