def equilateral(sides):
    return IsTriangle(*sides) and sides[0] == sides[1] == sides[2]  

def isosceles(sides):
    return IsTriangle(*sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])


def scalene(sides):
    return IsTriangle(*sides) and sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]

def IsTriangle(a,b,c):
    return a + b >= c and b + c >= a and a + c >= b and not TriangleSidesAreZero(a,b,c)

def TriangleSidesAreZero(a,b,c):
    return a == 0 and b == 0 and c == 0
