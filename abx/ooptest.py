#define 5 classes with atleast shish taking atleast 5 parameters
#and 3 objects
class Person:
    def __init__(self, name, age, email,location):
        self.name=name
        self.age=age
        self.email=email
        self.location=location

Person1= Person("tabshilla",42, "adongtm@gmail.com", "kira")
Person2= Person("pheona", 32, "pelyanu@gmail.com", "soroti")
print(Person1.name)
print(Person2.email)

class Student:
    def __init__(ozzy, name, age, email,location):
        ozzy.name=name
        ozzy.age=age
        ozzy.email=email
        ozzy.location=location

student1=Student("buyondo", 60, "student@refactory.com", "najjera")
print(student1.name)

class Animal:
    def __init__(self, name, color, size, gender, species):
        self.name=name
        self.color=color
        self.size=size
        self.gender=gender
        self.species=species

animal1=Animal("turtle", "blue", "large", "male", "mammal")

class Snake:
    def __init__(self, name, color, size, gender, species):
        self.name=name
        self.color=color
        self.size=size
        self.gender=gender
        self.species=species

snake2=Snake("python", "black", "large", "male", "reptile")
print(snake2.name)
print(snake2.species)

class Car:
    def __init__(self, name, color, size, brand):
        self.name=name
        self.color=color
        self.size=size
        self.brand=brand
car1 = Car("toyota", "black","small", "benz")
print(car1.brand)                                         

