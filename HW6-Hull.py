#  File: Hull.py

#  Description: Finds the smallest convex polygon that will enclose a given list of points

#  Student Name: Mercedes Milke

#  Partner Name: Mohamad Minoneshan

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 09/25/2022

#  Date Last Modified: 09/26/2022

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):

    # calculate the determinant of the 3x3 martix
    diag_down = (1 * q.x * r.y) + (p.x * q.y * 1) + (p.y * 1 * r.x)
    diag_up = (1 * q.x * p.y) + (r.x * q.y * 1) + (r.y * 1 * p.x)
    determinant = diag_down - diag_up

    return determinant

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):

    # creates the upper hull list and adds the first two points to it
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])

        while (len(upper_hull) >= 3) and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) > 0:
            del upper_hull[-2]

  # creates the lower hull list and adds the last two points to it
    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])

        while (len(lower_hull) >= 3) and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) > 0:
            del lower_hull[-2]

    # remove the first and last elements in the lower hull list to avoid duplicates
    del lower_hull[0]
    del lower_hull[-1]

    # combine the two lists
    convex_hull = upper_hull + lower_hull

    return convex_hull

# Input: convex_poly is  a list of Point objects that define the vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    determinant = convex_poly[-1].x * convex_poly[0].y - convex_poly[0].x * convex_poly[-1].y

    add = 0
    subtract = 0

    for i in range(len(convex_poly) - 1):
        add += (convex_poly[i].x * convex_poly[i + 1].y)
        subtract += (convex_poly[i + 1].x * convex_poly[i].y)

    determinant = determinant + add - subtract

    area = (1 / 2) * abs(determinant)

    return area

def main():

  # create an empty list of Point objects
  points_list = []

  # read number of points
  num_points = int(sys.stdin.readline().strip())

  # read data from standard input
  for i in range (num_points):
      line = sys.stdin.readline()
      line = line.strip().split()
      points_list.append (Point (int (line[0]), int (line[1])))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)
  #sorted_points = sorted(points_list,key=lambda x: (x[1]))
  '''
      # print the sorted list of Point objects
      for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  hull = convex_hull(sorted_points)

  # print your results to standard output
  # print the convex hull
  print('Convex Hull')

  for points in hull:
      print(points)
  
  print()

  # get the area of the convex hull
  area = area_poly(hull)

  # print the area of the convex hull
  print(f'Area of Convex Hull = {area}')

if __name__ == "__main__":
    main()
