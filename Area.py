A, B, C = input(). split(" ")

A = float(A)
B = float(B)
C = float(C)

# Triangulo Retangulo: Base*altura /2 
Triangulo =  (A*C)/2

AC =  (3.14159*(C**2))

AT = ((A+B)*C)/2

AQ = B*B

AR = A*B 

print(f'TRIANGULO: {Triangulo:.3f}')
print(f'CIRCULO: {AC:.3f}')
print(f'TRAPEZIO: {AT:.3f}')
print(f'QUADRADO: {AQ:.3f}')
print(f'RETANGULO: {AR:.3f}')