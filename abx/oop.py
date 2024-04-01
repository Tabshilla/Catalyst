#object oriented programming
#advocated for development of software  based on real world objects
#classes vs objects
#principles of opp
#polymorphism
#inheritance
#abstraction
#encapsulation

#a class is a blueprint of an object
#a blueprint is an original copy of something
#eg class car has an object such as benz, toyota.range rover
#class phone has an object iphone, tecno,itel
#objects take on the xtics of a class but each object has different attributes/xtics

#an object is an instance of a class
#how to identify a class of an object, use a phrase " is a"
#abstraction is the ability to ignore other details and concentrate on the highest level of representation
#abstract helps in identifying classes
class Chelsea:
    def palmer(self):
        print("palmer")
#class name must be singular e.g car not cars then the objects of class car are cars

#inheritance is where we have the concept of parent and child
#toyota is a child of the parent car. so class car is a parent of toyota
#inheritance is the ability for an object to take on different attributes of a class
#eg toyota wish is a child to toyota and yet toyota is a child to the class/parent  car

#polymorphism is the ability of an object to take on different attributes of a class
# polymorphism is the ability yo take on multiple forms
class WHT:
    def calc(self):
        wHt = 1000000 * 0.06
        return wHt
value = WHT()
print(value.calc())