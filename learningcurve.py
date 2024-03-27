#python has been quite interesting
#variable syntax for python(# represents a comment)
#e.g name = "tabshilla"
#print(name)
#datatypes in python
#This include numeric, string, sequencing, mapping, boolean, set
#Numeric:we have integers(int),float(float) and complex numbers(complex)
#examples:
# num1=10 int
# print(num1, "is a type of", type(num1))
# num2=2.4 float
# print(num1, "is of a type", type(num2))
# num3=1+2j complex 
# print(num3, "is of a type", type(num3))
#sequence data type
#under sequence, we have lists, tuples and range
# mylist=[]
# mylist.append("tabshilla")
# print(mylist)
# mylist.append(24)
# languages=["python","java", "javascript","C++","swift", "C", "cobol", "julia"]
# print(languages[7])

#tuples are not mutable, tuples are read only
#tuples can store more than one, tuples are identified by parentheses()
#an operator is a special character that tells a computer what to do with the value
#name= "tabshilla"
#operator  symbols and their meaning
#arithmetic operators(e.g.+,-,*,/,//)
#addition operators(+)
#subtraction operators(-)
#multiplication operators(*)
#division operators(/)
#floor division operators(//)
#modulo operator(%)
#exponential operator(**)
#assignment operator

#loops
##loops repeatedly do something until the condition is false 
#while loops 
#input
#for example
#name = input("plase enter here your name")
#while loop
# begin =1
# end  = 5
# while begin <= end:
#       print(begin)

#functions
#a named block of code is called a function
#defining a function 
#def loop1():
     #a block of code is a collection of related statements
     #a block of code is identified by identation
#calling a function
#loop1()
#This is a static function
#def loop(num1, num2):
    #a block of code is a collection of related statements
    #a block of code is identified by identation
    #print(num1 + num2)
#loop(5,5)
#(5,5) are parameters of a function
#this is a dynamic function

#global variables
#this can be used to return 
#they are not part of the function
#eg def add(a,b):
#     ans = a+b
#     print(ans)

# age = 25
# #parameters are inside the parentheses eg (a,b) a is a parameter as well as b
# def add1(a,b):
#     ans = a+b + age
#     age1 = 100

#     print(ans)
# #print(age1)
# add1(20,10)
#25 is a global variable

#classes and objects
#a class is a blueprint of an object
##an object is an instance of a class
#classes are declared first
#then the objects are declared after the class
#class Car
# name = ""
# color = ""
# size = ""
# engine = ""
# brand = "" 
#
# car = Toyota()
# car.name = "bluetec"
# car.color = "black"
# car.size = "small"
# car.engine = "combustion_engine"
# car.brand= "benz"

#accessing objects
# print(f"{car.name} is {car.color}")
# print(f"{car.name} is {car.brand}")

#or
#print(car.name  +  " is "  +  car.brand)
#functions in oop
#class Car
# name = ""
# color = ""
# size = ""
# engine = ""
# brand = "" 
# def move(self):
#         #print ("by driving)
#         return "by driving"
