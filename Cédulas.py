n=int(input(''))
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
print(n)
print(por100,'nota(s) de R$ 100,00')
print(por50,'nota(s) de R$ 50,00')
print(por20,'nota(s) de R$ 20,00')
print(por10,'nota(s) de R$ 10,00')
print(por5,'nota(s) de R$ 5,00')
print(por2,'nota(s) de R$ 2,00')
print(por1,'nota(s) de R$ 1,00')

