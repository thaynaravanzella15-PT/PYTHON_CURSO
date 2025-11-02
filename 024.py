cidade = input('Digite o nome de uma cidade: ')
print(cidade.find('santo'))
if cidade.find('santo') != -1:
    print('Tem santo')
else:
    print('Não tem santo')