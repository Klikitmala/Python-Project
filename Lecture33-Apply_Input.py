#price = 100
#vat = 7
#result = 100+(100*7/100)
#print(result)

price = int(input("Price(THB) ="))
vat = int(input("Vat(%) = "))
result = price+(price*vat/100)
print("Result=",result)