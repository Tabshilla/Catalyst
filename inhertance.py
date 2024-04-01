# class Animal:
#     def eat(self) -> None:
#         print ("I can eat")

# class Dog(Animal):
#     def display (self) -> None:
#         print ("my name is", self.name)
#         return "my name is " + self.name
# gshephered = Dog()
# gshephered.name = "police"
# print(gshephered.name)
# print(gshephered.display())
# print(gshephered.eat()) #inherited from parent  class

# a dog is a sub class of the class animal
#the dog in this case is the child/derived class and the animal class is referred to as the parent class

#assignment
#3 super classes with corresponding atleast 2 sub classes from each and create 3 objects from them

class Car:
    def drive(self) -> None:
        print ("I can move")

class Toyota(Car):
    def display (self) -> None:
        print ("my name is", self.name)
    
class Mercedes(Car):
    def display (self) -> None:
        print (f"{self.name} is a very fancy car")
        return None 
    

ty2 = Toyota()
ty2.name = "V8"
print(ty2.name)
print(ty2.display())
print(ty2.drive())

ty3 = Toyota()
ty3.name = "land_cruiser"
print(ty3.name)
print(ty3.display())
print(ty3.drive())

mrc1 = Mercedes()
mrc1.name = "GLE350"
print(mrc1.name)
print(mrc1.display())
print(mrc1.drive())

mrc2 = Mercedes()
mrc2.name = "ML350"
print(mrc2.name)
print(mrc2.display())
print(mrc2.drive())


class Snake:
    def bite(self) -> None:
        print ("I can bite you")

class Python(Snake):
    def display (self) -> None:
        print ("my name is", self.name)
        return None
              
class Anaconda(Snake):
    def display (self) -> None:
        print (f"{self.name} is a very dangerous snake")
        

snk1 = Python()
snk1.name = "ball_python"
print(snk1.name)
print(snk1.display())
print(snk1.bite())

snk3 = Python()
snk3.name = "borneo_python"
print(snk3.name)
print(snk3.display())
print(snk3.bite())

snk1 = Anaconda()
snk1.name = "ball_anaconda"
print(snk1.name)
print(snk1.display())
print(snk1.bite())

snk2 = Anaconda()
snk2.name = "burmese_anaconda"
print(snk2.name)
print(snk2.display())
print(snk2.bite())

class MotorBike:
    def vroom(self) -> None:
        print ("I can vroom")

class Scooter(MotorBike):
    def display (self) -> None:
        print ("my name is", self.name)
        return None

mbk1 = Scooter()
mbk1.name ="mechanical_scooter"
print(mbk1.name)
print(mbk1.display())
print(mbk1.vroom())

mbk2 = Scooter()
mbk2.name = "electric_scooter"
print(mbk2.name)
print(mbk2.display())
print(mbk2.vroom())



