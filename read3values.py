A, B, C = input("").split()

A=float(A)
B=float(B)
C=float(C)

if A+B>C and B+C>A:
    soma= A+B+C
    print(f'Perimetro = {soma:.1f}')


else:
    trapezio= ((A+B)*C)/2
    print(f"Area = {trapezio:.1f}")