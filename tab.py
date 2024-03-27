
#(range(1,10))
for i in range(1,10):
    print(i)
else:
    print("done")

list1 = [0,1,2,3,4,5,6]
for i in list1:
    print(i)
else:
    print("no items left")

def loop():
    x = 0

    while x <= 10:
        print(x)
        x += 3
    else:
        print("done")
loop()

def loop1():
    my_list = [10,20,30,40,50,60]

    for i in my_list:
        print(i)
    else:
        print("no more items left")
loop1()
#neso academy
some_string = 'Python is fun' 
print(some_string)

a, b, c = 5, 3.2, 'Hello'
print(c)

capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)

student_id = {112, 114, 116, 118, 115}
print(type(student_id))

numbers = (1, 2, 3)
print(numbers)

a = 7
b = 2
print ('Multiplication: ', a * b) 
print ('Division: ', a / b) 
print ('Floor Division: ', a // b)
print ('Modulo: ', a % b) 
print ('Power: ', a ** b)   
a = 10
b = 5
a += b  
print(a)
print('a < b =', a < b)
print('a > b =', a > b)
print('a == b =', a == b)
print('a >= b =', a >= b)
print('a <= b =', a <= b)
print((a > 2) and (b >= 6))
print(True and True)  
print(True and False)
print(True or False)
print(not True)

x1 = 5
y1 = 5
print(x1 is not y1) 

x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x2 is y2)
print(x3 is y3)

message = 'Hello world'
print('H' in message)
print('hello' not in message)

dict1 = {1:'a', 2:'b'}
print(1 in dict1)  
print('a' in dict1)
print('b' in dict1)
print(2 in dict1)

