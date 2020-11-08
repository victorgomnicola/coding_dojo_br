code1, units1, price1 = input().split()
units1 = int(units1)
price1 = float(price1)


code2, units2, price2 = input().split()
units2 = int(units2)
price2 = float(price2)

total = units1*price1 + units2*price2
print('VALOR A PAGAR: R$','{0:.2f}'.format(total))
