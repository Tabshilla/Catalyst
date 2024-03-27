class Lake:
        def __init__(self, name, location,depth,size, ltype):
              self.name = name
              self.location = location
              self.depth = depth
              self.size = size
              self.ltype = ltype
             
        
#creating objects of a class lake
lake1 = Lake("L.victoria", "jinja", "1000ft", "100m", "fresh_water")

#what is defined in the shish are  called parameters
#what is put after the .  is a property and what is after the = is a value
#the shish method(two underscores (__init_))
#the  first parameter in the shish parenthesis refers to an individual class or properties of an object
#self is not a parameter rather it defines the other parameters in the shish parenthesis.it determines the properties of the method
#the first one is an identifier
class River:
    def__init__(self,a, b, c):
    self.name = a
    self.location = b
    self.depth = c
river1 = River("nile", "jinja","600m")


