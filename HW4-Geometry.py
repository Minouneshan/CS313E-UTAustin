#  File: Geometry.py

#  Description: Program that takes in at least one x, y, and z coordinate representing a point 
#  or the center of either a sphere, a cube, or a cylinder in a 3D space;
#  and the height or radii of the shapes that they correspond to in order to simulate them in the given space.
#  It is possible to determine the surface area and volume of each shape,
#  as well as whether a second shape fits within the first, whether they’re intersecting,
#  or whether they’re not touching at all. 

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/11/2022

#  Date Last Modified: 9/16/2022

import math
import sys



class Point (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.center = [x,y,z]

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return '(' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + ')'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return float(math.dist([self.x,self.y,self.z], [other.x, other.y, other.z]))

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-6
        return ((abs(self.x-other.x) < tol) and (abs(self.y-other.y) < tol) and (abs(self.z-other.z) < tol))


class Sphere (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return 'Center: (' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + '), Radius: ' + str(float(self.radius))

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return float(4*math.pi*self.radius**2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return float(4/3*math.pi*self.radius**3)

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        center_coord = [self.x, self.y, self.z]
        point_coord = [p.x, p.y, p.z]

        return float(math.dist(center_coord, point_coord)) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):

        center_coord = [self.x, self.y, self.z]
        center2_coord = [other.x, other.y, other.z]

        return float(math.dist(center_coord, center2_coord)) < self.radius - other.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):

        center_coord = [self.x, self.y, self.z]
        center2_coord = [a_cube.x, a_cube.y, a_cube.z]
        half_diag = (a_cube.side*(3**0.5))/2

        return float(math.dist(center_coord, center2_coord)) < self.radius - half_diag

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        out = False

        if float(math.hypot(self.x - a_cyl.x, self.y - a_cyl.y)) < self.radius - a_cyl.radius:
            if abs(self.z - a_cyl.z) < self.radius - a_cyl.height/2:
                out = True

        return out

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        center_coord = [self.x, self.y, self.z]
        center2_coord = [other.x, other.y, other.z]
        out = False
        if float(math.dist(center_coord, center2_coord)) >= self.radius - other.radius:
            if float(math.dist(center_coord, center2_coord)) <= self.radius + other.radius:
                out = True
        return out

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):

        center_coord = [self.x, self.y, self.z]
        center2_coord = [a_cube.x, a_cube.y, a_cube.z]
        half_diag = (a_cube.side*(3**0.5))/2
        out = False
        if float(math.dist(center_coord, center2_coord)) >= self.radius - half_diag:
            if float(math.dist(center_coord, center2_coord)) <= self.radius + half_diag:
                out = True

        return out

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        c_object = Cube()
        c_object.side = self.radius * (2/math.sqrt(3))
        c_object.center = Point(self.x,self.y,self.z)

        return c_object


class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.side = side
        self.center = Point(x,y,z)
        self.x = x
        self.y = y
        self.z = z

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return 'Center: (' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + '), Side: ' + str(float(self.side))

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return float(6*self.side**2)

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return float(self.side**3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        out = False
        if self.x-self.side/2 < p.x < self.x + self.side/2:
            if self.y-self.side/2 < p.y < self.y + self.side/2:
                if self.z-self.side/2 < p.z < self.z + self.side/2:
                    out = True
        return out

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        center_coord = [self.x, self.y, self.z]
        center2_coord = [a_sphere.x, a_sphere.y, a_sphere.z]

        if float(math.dist(center_coord, center2_coord)) <= self.side/2 - a_sphere.radius:
            out = True
        else:
            out = False
        return out

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        x2 = other.x
        y2 = other.y
        z2 = other.z
        side = other.side
        lst = [[x2+side/2, y2-side/2, z2+side/2], [x2+side/2, y2+side/2, z2+side/2],\
            [x2-side/2, y2-side/2, z2+side/2], [x2-side/2, y2+side/2, z2+side/2],\
            [x2+side/2, y2+side/2, z2-side/2], [x2+side/2, y2-side/2, z2-side/2],\
            [x2-side/2, y2+side/2, z2-side/2], [x2-side/2, y2-side/2, z2-side/2]]
        out = True
        for i in range(0,8):
            p = Point(lst[i][0], lst[i][1], lst[i][2])
            if not self.is_inside_point(p):
                out = False
                break
        return out

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        out = False

        if float(math.hypot(self.x - a_cyl.x, self.y - a_cyl.y)) < self.side/2 - a_cyl.radius:
            if abs(self.z - a_cyl.z) < self.side/2 - a_cyl.height/2:
                out = True

        return out

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        x = self.x
        y = self.y
        z = self.z
        side = self.side
        x2 = other.x
        y2 = other.y
        z2 = other.z
        side2 = other.side
        lst = [[x+side/2, y-side/2, z+side/2], [x+side/2, y+side/2, z+side/2],\
            [x-side/2, y-side/2, z+side/2], [x-side/2, y+side/2, z+side/2],\
            [x+side/2, y+side/2, z-side/2], [x+side/2, y-side/2, z-side/2],\
            [x-side/2, y+side/2, z-side/2], [x-side/2, y-side/2, z-side/2]]
        lst2 = [[x2+side2/2, y2-side2/2, z2+side2/2], [x2+side2/2, y2+side2/2, z2+side2/2],\
            [x2-side2/2, y2-side2/2, z2+side2/2], [x2-side2/2, y2+side2/2, z2+side2/2],\
            [x2+side2/2, y2+side2/2, z2-side2/2], [x2+side2/2, y2-side2/2, z2-side2/2],\
            [x2-side2/2, y2+side2/2, z2-side2/2], [x2-side2/2, y2-side2/2, z2-side2/2]]
        
        counter = 0
        counter2 = 0
        out = False
        for i in range(0,8):
            p = Point(lst2[i][0], lst2[i][1], lst2[i][2])
            if not self.is_inside_point(p):
                counter2 += 1
        if counter2 > 0 and counter2 < 8:
            out = True
        
        if not out:    
            for i in range(0,8):
                p = Point(lst[i][0], lst[i][1], lst[i][2])
                if not other.is_inside_point(p):
                    counter += 1
            if counter > 0 and counter < 8:
                out = True

        return out

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        x = self.x
        y = self.y
        z = self.z
        side = self.side
        x2 = other.x
        y2 = other.y
        z2 = other.z
        side2 = other.side
        cx = side/2 + side2/2 - abs(x - x2)
        cy = side/2 + side2/2 - abs(y - y2)
        cz = side/2 + side2/2 - abs(z - z2)
        volume = cx * cy * cz
        return volume

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object

    def inscribe_sphere(self):
        s_object = Sphere()
        s_object.x = self.x
        s_object.y = self.y
        s_object.z = self.z
        s_object.radius = self.side/2
        s_object.center = Point(self.x,self.y,self.z)

        return s_object


class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self,x=0, y=0, z=0,radius=1, height=1):
        self.radius = radius
        self.height = height
        self.center = Point(x,y,z)
        self.x = x
        self.y = y
        self.z = z

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return 'Center: (' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + '), Radius: ' + str(float(self.radius)) + ', Height: ' + str(float(self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return (2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius**2)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return (math.pi * self.radius**2 * self.height)

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        out = False
        if p.z > self.z-self.height/2 and p.z < self.z + self.height/2:
            if float(math.hypot(self.x - p.x, self.y - p.y)) < float(self.radius):
                out = True
        return out

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        out = False

        if float(math.hypot(self.x - a_sphere.x, self.y - a_sphere.y)) < self.radius - a_sphere.radius:
            if abs(self.z - a_sphere.z) < self.height/2 - a_sphere.radius:
                out = True

        return out

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean

    def is_inside_cube(self, a_cube):
        out = False

        if float(math.hypot(self.x - a_cube.x, self.y - a_cube.y)) < self.radius - a_cube.side/2:
            if abs(self.z - a_cube.z) < self.height/2 - a_cube.side/2:
                out = True

        return out

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean

    def is_inside_cylinder(self, other):
        out = False

        if float(math.hypot(self.x - other.x, self.y - other.y)) < self.radius - other.radius:
            if abs(self.z - other.z) < self.height/2 - other.height/2:
                out = True

        return out

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean

    def does_intersect_cylinder(self, other):
        out = False

        if float(math.hypot(self.x - other.x, self.y - other.y)) >= self.radius - other.radius:
            if float(math.hypot(self.x - other.x, self.y - other.y)) <= self.radius + other.radius:
                if abs(self.z - other.z) <= self.height/2 - other.height/2:
                    out = True
        if abs(self.z - other.z) >= self.height/2 - other.height/2:
            if abs(self.z - other.z) <= self.height/2 + other.height/2:
                out = True

        return out


def main():
  # read data from standard input
    x = sys.stdin.read()
    a = x.split("\n")
    for elem in range(len(a)):
        a[elem] = a[elem].split()

    origin = Point(0, 0, 0)

    # create a Point object
    p = Point(float(a[0][0]), float(a[0][1]), float(a[0][2]))

    # create a Point object
    q = Point(float(a[1][0]), float(a[1][1]), float(a[1][2]))

    # create a Sphere object A
    sphereA = Sphere(float(a[2][0]), float(a[2][1]),
                     float(a[2][2]), float(a[2][3]))

    # create a Sphere object B
    sphereB = Sphere(float(a[3][0]), float(a[3][1]),
                     float(a[3][2]), float(a[3][3]))

    # create a Cube object A
    cubeA = Cube(float(a[4][0]), float(a[4][1]),
                 float(a[4][2]), float(a[4][3]))

    # create a Cube object B
    cubeB = Cube(float(a[5][0]), float(a[5][1]),
                 float(a[5][2]), float(a[5][3]))

    # create a Cylinder object A
    cylA = Cylinder(float(a[6][0]), float(a[6][1]), float(
        a[6][2]), float(a[6][3]), float(a[6][4]))

    # create a Cylinder object B
    cylB = Cylinder(float(a[7][0]), float(a[7][1]), float(
        a[7][2]), float(a[7][3]), float(a[7][4]))

    # print if the distance of p from the origin is greater than the distance of q from the origin
    if p.distance(origin) > q.distance(origin):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    # print if Point p is inside sphereA
    if sphereA.is_inside_point(p) is True:
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB) is True:
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA) is True:
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA) is True:
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB) is True:
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")

    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB) is True:
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA
    cubeC = sphereA.circumscribe_cube()
    if cubeC.volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    # print if Point p is inside cubeA
    if cubeA.is_inside_point(p) is True:
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA) is True:
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB) is True:
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA) is True:
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print(
            "Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA
    sphereC = cubeA.inscribe_sphere()
    if sphereC.area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

    # print if Point p is inside cylA
    if cylA.is_inside_point(p) is True:
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA) is True:
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA) is True:
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB) is True:
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB) is True:
        print("cylB does intersect cylA")
    else:
        print('cylB does not intersect cylA')


if __name__ == "__main__":
    main()
