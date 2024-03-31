import math
A, B, C = input(). split(" ")
A = float(A)
B = float(B)
C = float(C)
 
if A>0:
    delta=(B**2)-(4*(A*C))
    if delta>0:
        x1=((-B)+(math.sqrt(delta)))/(2*A)
        x2=((-B)-(math.sqrt(delta)))/(2*A)
        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')