item, quantidade = input( ). split(" ")

item=int(item)
quantidade=int(quantidade)

if item==1:
    preco=4.00
    print(f'Total: R$ {preco*quantidade:.2f}')

if item==2:
    preco=4.50
    print(f'Total: R$ {preco*quantidade:.2f}')


if item==3:
    preco=5.00
    print(f'Total: R$ {preco*quantidade:.2f}')


if item==4:
    preco=2.00
    print(f'Total: R$ {preco*quantidade:.2f}')


if item==5:
    preco=1.50
    print(f'Total: R$ {preco*quantidade:.2f}')


elif item > 5:
    print('Valor Inválido')

