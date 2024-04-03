# class Parent:
#     def __init__(self, name, tribe,  clan, religion):
#         self.name = ""
#         self.tribe =""
#         self.clan =""
#         self.religion =""

# class Child(Parent):
#     pass
# first_born = Child("adong", "itesot", "munyaks", "catholic")
# print(child.name)
        

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname, self.lastname)
x=Person("john", "doe")
x.printname()

class Student(Person):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
x=Student("tabshilla", "doe")

x.printname()