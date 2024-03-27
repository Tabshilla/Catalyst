def add():
    num1, num2, = 10, 20
    sum = num1 + num2
    print(sum)
add()

#creating a dynamic funtion
def add1(num1, num2):
    sum = num1 + num2
    print(sum)

add1(100, 50)
add1(200, 45)
add1(45,75)

def sub1(num1, num2):
    sub = num1 - num2
    print(sub)

sub1(100, 50)
sub1(200, 45)
sub1(45,75)

def mul1(num1, num2):
    mul = num1 * num2
    print(mul)

mul1(100, 50)
mul1(200, 45)
mul1(45,75)


def div1(num1, num2):
    div = num1 / num2
    print(div)

div1(100, 50)
div1(200, 45)
div1(45,75)

def floordiv(num1, num2):
    floordiv = num1 // num2
    print(floordiv)

floordiv(100, 50)
floordiv(200, 45)
floordiv(45,75)

def mod1(num1, num2):
    mod = num1 % num2
    print(mod)

mod1(100, 50)

def pow1(num1, num2):
    pow = (num1 **2)
    print(pow)

pow1(100, 50)

def multidata(num1, num2, name, float):
    print(num1) 
    print(num2) 
    print(name) 
    print(float)
multidata(10,50, "tabshilla", 0.5)


def data(country, num2, name, complex, int):
    print(country) 
    print(num2) 
    print(name) 
    print(complex)
    print(int)
data("uganda",50, "pheona", 2+1j, 40)

def hack(name, yob,district):
    #print(name) 
    #print(yob) 
    #print(district) 
    currentYear = 2024
    age = currentYear - yob
    print(name, "is", age)

hack("adong",2001, "soroti")

