def speed(distance, time):
    speed = distance / time
    return speed

speed(10, 2)

def distance(speed, time):
    distance = speed * time
    return distance

distance(5, 2)


def speed1():
    speed2 =distance(5,2)
    new_speed = speed2 + 1000
    print(new_speed)

speed1()


def area(length, width):
    area = length * width
    return area

area(50, 25)

def vol(area, height):
    vol = area * height
    return vol

vol(50, 25)

def area1():
    area2 = vol(50, 25)
    new_area = area2 * 2
    print(new_area)
area1()

    