cod_peça , Num_peças, Valor_uni = input(). split(" ")
cod_peça2 , Num_peças2 , Valor_uni2 =input(). split(" ")

cod_peça = int(cod_peça)
Num_peças = int(Num_peças)
Valor_uni = float(Valor_uni)

cod_peça2 = int(cod_peça2)
Num_peças2 = int(Num_peças2)
Valor_uni2 = float(Valor_uni2)

calculop1=Num_peças*Valor_uni
calculop2=Num_peças2*Valor_uni2
ValorPago= calculop1+calculop2

print(f'VALOR A PAGAR: R$ {ValorPago:.2f}')