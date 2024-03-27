#defining an object in python
#we use the keyword "class"  followed by the name starting with a capital letter, ending with a full colon

class Animal:
    name = ""
    color = ""
    size = ""
    sound = ""
    gender = "" 
    species = ""
    age = 0
    def feed(self):
        #print ("by chewing")
        return "by chewing"
#the above is a method
#a function of a class is called a method
#a function defined within a class is called a method
#creating objects of a class animal
#a complete fulfilment of attributes form an object
cat = Animal()
cat.name = "tom"
cat.color = "brown"
cat.size = "medium"
cat.sound = "moew"
cat.gender = "female"
cat.species = "mammal"
cat.age = 17
cat.feed()
#accessing objects
print(f"{cat.name} is {cat.age} years old")
print(f"{cat.name} is {cat.gender}")
print(cat.name  +  " does "  +  cat.sound)
print(f"{cat.name} is {cat.species}")
print(cat.name + " is " + cat.size)
print(f"{cat.feed()}")
print(cat.name  +  " feeds "  +  cat.feed())

dog = Animal()
dog.name = "sky"
dog.size = "medium"
dog.sound = "bark"
dog.gender = "male"
dog.age = 20

print(f"{dog.name} is {dog.size}")