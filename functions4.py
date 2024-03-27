def vat(rate, price):
    frate = int((rate/100) * price)
    return frate

    print(frate)
print(vat(18,20000))


def act_price():
    actvat = vat(18, 20000)
    print(actvat)
    netprice = actvat + 20000
    print(netprice)

act_price()
#assignemt
#using fundermentalized function create three functions that share values. the last function should print out
#two of them should be dynamic
#last one should be receiving values from


