n1, n2, n3, n4 = input( ). split(" ")

n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)

avg=((n1*2)+(n2*3)+(n3*4)+(n4*1))/(1+2+3+4)
print(f'Media: {avg:.1f}')

if avg>7:
    print("Aluno aprovado.")
if avg<5:
    print("Aluno reprovado.")
    
if avg>5 or avg==5 and avg <7 or avg==7:
    print("Aluno em exame.")
    ne=float(input(''))
    print("Nota do exame: ",ne)
    avgpos=(ne+avg)/2 
    if avgpos>5:
        print("Aluno aprovado.")
    if avgpos<4.9:
        print("Aluno reprovado.")
    print('Media final: ',avgpos)