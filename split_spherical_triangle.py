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
