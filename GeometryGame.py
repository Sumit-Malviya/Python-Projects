#Problem Statement:-

'''

1. To check whether a given coordinate falls within a random
rectangle drawn with lower left and upper right coordinates.

2. Also check the distance of your point object with a point 
taken as an input from user.

'''

#class Point to create various point objects

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y


  #Method falls_in_rectangle to check position of point w.r.t 
  # lower left and upper right coordinate of rectangle
    
  def falls_in_rectangle(self, lower_left_point, upper_right_point):
    if lower_left_point[0] < self.x < upper_right_point[0] \
    and lower_left_point[1] < self.y < upper_right_point[1]:
      return True
    else:
      return False
    

  #Method distance to calcualte distance of an object from
  # a random point given by user
     
  def distance_from_another_point(self, point):
    distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    return distance


# Use cases:-
  
point1 = Point(2, 4)
falls = point1.falls_in_rectangle((1, 3), (5, 6))
print(falls)

point2 = Point(1, 2)
dist = round(point1.distance_from_another_point(point2), 2)
print(dist)