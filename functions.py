#a named block of code is called a function
# a named group of statements is a function
#functions are the building blocks of programming languages
#for example 
def my_function():
    num1, num2, = 20, 40
    print(num1 + num2)
#function call
my_function()

#we have 2 types of functions; static functions and dynamic functions
#static functions have empty parentheses
#dynamic functions have values inside them

#conditional functions
def condition():
    num = 10
    if num > 0:
        print("num is positive")
    print("if the if statement is easy")
#condition()
#below code has been extracted from the function 
num = 20
if num > 0:
    print("num is positive")

def my_condition():
    num = -10
    if num > 0:
        print("num is positive")
    else:
        print("num is negative")
    print("this statement is not related to if or esle but in the same function")


my_condition()

