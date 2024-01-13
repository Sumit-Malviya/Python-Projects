# Problem Statement:-

'''
1. To check whether a given coordinate falls within a random
rectangle drawn with lower left and upper right coordinates.

2. Also check the distance of your point object with a point 
taken as an input from user.
'''
import turtle
# imports
from random import randint
from turtle import Turtle

# Initializing turtle object
myturtle = Turtle()
mypointturtle = Turtle()


# class Point to create various point objects

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method falls_in_rectangle to check position of point w.r.t lower left and upper right coordinate of rectangle

    def falls_in_rectangle(self, rectangle):
        if rectangle.lower_left_point.x < self.x < rectangle.upper_right_point.x \
          and rectangle.lower_left_point.y < self.y < rectangle.upper_right_point.y:
            return True
        else:
            return False

    # Method distance to calculate distance of an object from
    # a random point given by user

    def distance_from_another_point(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance


# class Rectangle

class Rectangle:

    def __init__(self, lower_left_point, upper_right_point):
        self.lower_left_point = lower_left_point
        self.upper_right_point = upper_right_point

    # method to find area of rectangle
    def area_of_rectangle(self):
        return ((self.upper_right_point.x - self.lower_left_point.x) \
                * (self.upper_right_point.y - self.lower_left_point.y))

    # Use cases:-


# User inputs
user_x = float(input("Enter one X coordinate: "))
user_y = float(input("Enter one Y coordinate: "))

# Object initialization
pointx = Point(user_x, user_y)

print(f"\nUser's guessed points are: ({pointx.x}, {pointx.y})")

# Generating random points
random_point1 = Point(randint(1, 9), randint(1, 9))
random_point2 = Point(randint(10, 19), randint(10, 19))



print(
    f"\nThe two random points of rectangle are: ({random_point1.x}, {random_point1.y}) and ({random_point2.x}, {random_point2.y})")

# Object initialization
rectanglex = Rectangle(random_point1, random_point2)

# method implementation on object
falls = pointx.falls_in_rectangle(rectanglex)

print(f"\nUser's guessed point lie within the rectangle: {falls}")

# method implementation on object
areax = rectanglex.area_of_rectangle()
print(f"The area of rectangle is: {areax}")

# Object initialization
point1 = Point(1, 2)

# method implementation on object
dist = round(pointx.distance_from_another_point(point1), 2)
print(f"\nDistance of point ({point1.x}, {point1.y}) with user's point ({pointx.x}, {pointx.y}): {dist}")


myturtle.penup()
myturtle.goto(random_point1.x, random_point1.y)
myturtle.pendown()
myturtle.forward(random_point2.x - random_point1.x)
myturtle.left(90)
myturtle.forward(random_point2.y - random_point1.y)
myturtle.left(90)
myturtle.forward(random_point2.x - random_point1.x)
myturtle.left(90)
myturtle.forward(random_point2.y - random_point1.y)

mypointturtle.penup()
mypointturtle.goto(user_x, user_y)
mypointturtle.pendown()
mypointturtle.dot(5, 'red')

turtle.done()