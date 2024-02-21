import math

def score(x, y):
    radius_units = CalculateRadiusUnits(x,y)
    if radius_units <= 1 : return 10
    elif 1 < radius_units <= 5: return 5
    elif 5 < radius_units <= 10: return 1
    else : return 0

def CalculateRadiusUnits(coor_x, coor_y):
    return math.sqrt(coor_x*coor_x + coor_y*coor_y)
