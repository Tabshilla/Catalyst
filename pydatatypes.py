#datatypes in python
#numeric
#string
#sequencing
#mapping
#boolean
#set


#Numeric:we have integers(int),float(float) and complex numbers(complex)
#examples:
num1=10
print(num1, "is a type of", type(num1))
num2=2.4
print(num1, "is of a type", type(num2))

num3=1+2j
print(num3, "is of a type", type(num3))

num1 = 100
#float
#valus with decimal places
int(num1)
print(num1)



#sequence data type
#under sequence, we have lists, tuples and range
#lists

mylist=[]
mylist.append("tabshilla")
print(mylist)
mylist.append(24)
print(mylist)
languages=["python","java", "javascript","C++","swift", "C", "cobol", "julia"]
print(languages[7])
print(languages[2])
print(languages[3])
print(languages[0],languages[3])
print(languages[-1])

#tuples are not mutable.
#tuples are read only
#tuples can store more than one
#tuples are identified by parentheses()


world=[["uganda","kenya","tanzania"], ["south africa","namibia","zambia",["england"]], ["tunisia","egypt"],"brazil", "USA"]

print(world[0][2])
print(world[1][1])
print(world[1][-1])
print(world[1][3][0])

country=["nigeria", "ghana","chad", "niger"], ["eritrea","ethipia","sudan" ], ["canada", "USA", "mexico",["alaska"], "portugal","france"]
print(country[0][1])
print(country[-1])
print(country[-1][1])
print(country[-1][-2][-3])
print(country[2][0])
print(country[2][3])
print(country[2][3][0])
print(country[2][4])






uganda = {"name": "uganda", "popn":45, "loc":"east africa"}
print(type(uganda))
print(uganda.keys())
print(uganda.values())

my_numbers = {10, 20, 30, 40, 10, 30}
print(my_numbers) 
student_id = {200, 300, 400, 500, 600, 600, 400, 400, 400, 400}
print(student_id)

lakes ={"name":"victoria", "location":"uganda", "length":120, "source":"nile"}
for keys, value in lakes.items():
    print(keys, value)








