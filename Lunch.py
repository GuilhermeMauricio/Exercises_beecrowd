id=int(input('Insira o código do alimento: '))
quantidade= float(input('Insira a quantidade de itens: '))

if id==1:
    preco=4.00
    print(f'Total: R$ {preco*quantidade:.2f}')

if id==2:
    preco=4.50
    print(f'Total: R$ {preco*quantidade:.2f}')


if id==3:
    preco=5.00
    print(f'Total: R$ {preco*quantidade:.2f}')


if id==4:
    preco=2.00
    print(f'Total: R$ {preco*quantidade:.2f}')


if id==5:
    preco=1.50
    print(f'Total: R$ {preco*quantidade:.2f}')


elif id > 5:
    print('Valor Inválido')