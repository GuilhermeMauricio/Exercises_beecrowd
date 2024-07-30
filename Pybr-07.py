product1=float(input('Insert the price of the first product: '))
product2=float(input('Insert the price of the second product: '))
product3=float(input('Insert the price of the third product: '))


if product1<product2 and product1<product3:
    print('the first is the cheapest product')
elif product2<product1 and product2<product3:
    print('the second is the cheapest product')
elif product3<product1 and product3<product2:
    print('the third is the cheapest product')