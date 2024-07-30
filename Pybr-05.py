n1= float(input('Insira a primeira nota: '))
n2=float(input('Insira a segunda nota: '))
media= (n1+n2)/2

if media>=7:
    if media ==10:
        print('Aprovado com Distinção!')
    else:
        print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')