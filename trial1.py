"""def identify(name, age, email, gender):
    print(name)
    print(age)
    print(email)
    print(gender)
identify( name = input("type your name here"),age = input("type your age here"),email = input("type your email here"),gender= input("type your gender here"))
"""
"""def name():
    Block
    return

"""
# net_pay = grosspay - nssf - paye
# nssf = grosspay * rate
# paye = grosspay * rate

# def identify(name, age, gender, email):
#     name = input("type your name here")
#     age = input("type your age here")
#     gender = input("type your gender here")
#     email = input("type your email here")
#     print([name, age, gender, email])
#     return [name, age, gender, email]

# print (identify("name", "age", "gender", "email"))

# def net_pay(paye,nssf,gross_amount):
#     paye = int(input("paye: "))
#     nssf = int(input("nssf: "))
#     gross_amount = int(input("gross_amount: "))
#     nssf1 = (nssf/100) * gross_amount
#     paye1 = (paye/100) * gross_amount
#     net_pay = gross_amount -int( nssf1 + paye1)
#     return net_pay

# print(net_pay("paye","nssf", "gross_amount"))

def net_pay1(paye = int(input("paye: ")), nssf = int(input("nssf: ")), gross_amount = int(input("gross_amount: "))):
    paye1 = (paye/100) * gross_amount
    nssf1 = (nssf/100) * gross_amount
    net_pay = gross_amount -int( nssf1 + paye1)
    print('..............................')
    return net_pay

print(net_pay1())




