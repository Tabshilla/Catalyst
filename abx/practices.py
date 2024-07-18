# colors = ['red', 'green', 'blue', 'white']
# for i in range(3):
#     print(colors[i])

def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(5, 3)
print("Result:", result)

# def calculate_average(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     average = total / len(numbers)  # Error: Division by zero
#     return average

# numbers = [1, 2, 3, 4, 5]
# average = calculate_average(numbers)
# print("Average:", average)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

for char in "hello":
    print(char)

for c in "color":
    print(c)

set1 = {1,2,3}
set2= {3,4,5}
print(set1 - set2)

class Bird:
    def printSize(self):
        print('small')

class Eagle(Bird):
    def printSize(self):
        print('large')

bird = Bird()
bird.printSize()

eagle = Eagle()

eagle.printSize()

x = 5
def func():
    global x
    x += 1
    print(x)
func()
    



