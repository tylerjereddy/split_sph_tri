'''
The purpose of this module is to produce the coordinates of
the point that splits a spherical triangle into 3 subtriangles
of equal area.

Resources:
https://math.stackexchange.com/questions/1730002/how-to-divide-a-spherical-triangle-into-three-equal-area-spherical-triangles
https://www.researchgate.net/file.PostFileLoader.html?id=5745b2c2615e27f83f50d7a1&assetKey=AS%3A365634799063048%401464185537995

Mostly using equation designations from the second resource above.
'''
import math
from __future__ import division

def y_angle(t_19, t_18, t_20):
    '''Returns subtriangle angle y.'''
    numerator = - (t_19 - t_18)
    denominator = 2. * t_20
    y = math.atan(numerator / denominator)
    return y

def t_1(angle_c, subtriangle_area):
    '''Returns the value of t_1.'''
    result = math.cos(angle_c - subtriangle_area) - \
             math.cos(angle_c)
    return result

def t_2(angle_c, subtriangle_area):
    '''Returns the value of t_2.'''
    result = math.sin(angle_c - subtriangle_area) - \
             math.sin(angle_c)
    return result

def t_3(angle_c, arc_length_A, subtriangle_area):
    '''Returns the value of t_3.'''
    result = math.sin(angle_c - subtriangle_area) - \
             math.cos(arc_length_A) * math.sin(angle_c)
    return result

def t_4(angle_c, arc_length_A, subtriangle_area):
    '''Returns the value of t_4.'''
    result = math.cos(arc_length_A) * math.cos(angle_c) - \
             math.cos(angle_c - subtriangle_area)
    return result

def t_5(angle_a, subtriangle_area):
    '''Returns the value of t_5.'''
    result = math.cos(angle_a - subtriangle_area) - \
             math.cos(angle_a)
    return result

def t_6(angle_a, subtriangle_area):
    '''Returns the value of t_6.'''
    result = math.sin(angle_a - subtriangle_area) - \
             math.sin(angle_a)
    return result

def t_9(angle_b, subtriangle_area):
    '''Returns the value of t_9.'''
    result = math.cos(angle_b - subtriangle_area) - \
             math.cos(angle_b)
    return result

def t_10(angle_b, subtriangle_area):
    '''Returns the value of t_10.'''
    result = math.sin(angle_b - subtriangle_area) - \
            math.sin(angle_b)
    return result

def t_11(angle_b, subtriangle_area, arc_length_C):
    '''Returns the value of t_11.'''
    result = math.sin(angle_b - subtriangle_area) - \
             math.cos(arc_length_C) * math.sin(angle_b)
    return result

def t_12(angle_b, subtriangle_area, arc_length_C):
    '''Returns the value of t_12.'''
    result = math.cos(arc_length_C) * math.cos(angle_b) - \
             math.cos(angle_b - subtriangle_area)
    return result

def t_15(t_3, t_7, t_4, t_5):
    '''Returns the value of t_15.'''
    result = t_3 * t_7 + t_4 * t_5
    return result

def t_16(t_3, t_8, t_4, t_6):
    '''Returns the value of t_16.'''
    result = t_3 * t_8 + t_4 * t_6
    return result

def t_18(t_13, t_12, t_14, t_10):
    '''Returns the value of t_18.'''
    result = t_13 * t_12 + t_14 * t_10
    return result

def t_19(t_15, t_11, t_16, t_9):
    '''Returns the value of t_19.'''
    result = t_15 * t_11 + t_16 * t_9
    return result

def t_20(t_15, t_12, t_16, t_10):
    '''Returns the value of t_20.'''
    result = t_15 * t_12 + t_16 * t_10
    return result
