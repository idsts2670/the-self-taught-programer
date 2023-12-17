import math

# object oriented programming practice P156
# challenge 1
class Apple:
    def __init__(self, c, w, s, sw):
        self.color = c
        self.wegight = w
        self.size = s
        self.sweetness = sw

# chllange 2
## create a circle class with an area method
class Circle:
    def __init__(self, r):
        self.radium = r
    
    def area(self):
        return self.radium ** 2 * math.pi

# Circle object test
circle = Circle(2)
print('Challenge 2:')
print(circle.area())

# challenge 3
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2

# return the area of triangle
triangle = Triangle(2, 3)
print('Challenge 3:')
print(triangle.area())

# challenge 4
class Hexagon:
    def __init__(self, l):
        self.length = l
    
    # calculate the perimeter of hexagon
    def calculate_perimeter(self):
        return self.length * 6

hexagon = Hexagon(2)
print('Challenge 4:')
print(hexagon.calculate_perimeter())



# Encapsulation is the process of keeping multiple variables and methods within a single class by using some objects
# http://tinyurl.com/j74o5rh

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len
    
# Encapsulation is also the process of hiding the inner working or the data of an object from the outside world.
# http://tinyurl.com/jtz28ha

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    # example of private method. In this way, client can't access the data within the class
    def change_data(self, index, n):
        self.nums[index] = n

# these return the same result
data_one = Data()
data_one.nums[0]  = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)
