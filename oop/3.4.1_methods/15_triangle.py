'''
Distance formula of triangle in python
√(x2 − x1)2 + (y2 − y1)2
'''


import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return math.hypot(dx, dy)

    def distance_from_point(self, point):
        dx = self.__x - point.getx()
        dy = self.__y - point.gety()
        return math.hypot(dx, dy)


class Triangle:

    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        a = ((self.__points[0].getx() - self.__points[1].getx()) ** 2 + (
                    self.__points[0].gety() - self.__points[1].gety()) ** 2) ** 0.5
        b = ((self.__points[1].getx() - self.__points[2].getx()) ** 2 + (
                    self.__points[1].gety() - self.__points[2].gety()) ** 2) ** 0.5
        c = ((self.__points[2].getx() - self.__points[0].getx()) ** 2 + (
                    self.__points[2].gety() - self.__points[0].gety()) ** 2) ** 0.5
        return a + b + c


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())



