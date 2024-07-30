Number1=float(input('Insira o primeiro numero: '))
Number2=float(input('Insira o segundo numero: '))
Number3=float(input('Insira o terceiro numero: '))

if Number1>Number2 and Number1>Number3:
    print('Primeiro Número é o maior')
elif Number2>Number1 and Number2>Number3:
    print('Segundo Número é maior')
elif Number3>Number1 and Number3>Number2:
    print('Terceiro Número é maior')
else:
    print('Entrada inválida! ')

if Number1<Number2 and Number1<Number3:
    print('Primeiro Número é o menor')

elif Number2<Number1 and Number2<Number3:
    print('Segundo Número é o menor')

elif Number3< Number1 and Number3<Number2:
    print('Primeiro Número é o menor')