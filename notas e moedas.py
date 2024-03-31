n=float(input(''))
por100=int(n/100)
resto=n%100
por50=int(resto/50)
resto2=resto%50
por20=int(resto2/20)
resto3=resto2%20
por10=int(resto3/10)
resto4=resto3%10
por5=int(resto4/5)
resto6=resto4%5
por2=int(resto6/2)
resto7=resto6%2
por1=int(resto7/1)
resto8=resto7%1

#MOEDAS


Mpor1=int(resto7/1)
Mpor_50=int((resto7%1)/0.50)
Mpor_25=int(((resto7%1)%0.50)/0.25)
Mpor__10=int((((resto7%1)%0.50)%0.25)/0.10)
Mpor_05=int(((((resto7%1)%0.50)%0.25)%0.10)/0.05)
Mpor_01=int((((((resto7%1)%0.50)%0.25)%0.10)%0.05)/0.01)



print("NOTAS:")
print(por100,'nota(s) de R$ 100.00')
print(por50,'nota(s) de R$ 50.00')
print(por20,'nota(s) de R$ 20.00')
print(por10,'nota(s) de R$ 10.00')
print(por5,'nota(s) de R$ 5.00')
print(por2,'nota(s) de R$ 2.00')

print("MOEDAS:")
print(Mpor1,'moeda(s) de R$ 1.00')
print(Mpor_50,'moeda(s) de R$ 0.50')
print(Mpor_25,'moeda(s) de R$ 0.25')
print(Mpor__10,'moeda(s) de R$ 0.10')
print(Mpor_05,'moeda(s) de R$ 0.05')
print(f'{Mpor_01} moeda(s) de R$ 0.01')




