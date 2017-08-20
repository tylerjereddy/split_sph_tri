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

def t_7(angle_a, subtriangle_area, arc_length_B):
    '''Returns the value of t_7.'''
    result = math.sin(angle_a - subtriangle_area) - \
             math.cos(arc_length_B) * math.sin(angle_a)
    return result

def t_8(angle_a, subtriangle_area, arc_length_B):
    '''Returns the value of t_8.'''
    result = math.cos(arc_length_B) * math.cos(angle_a) - \
             math.cos(angle_a - subtriangle_area)
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

def t_13(t_1, t_7, t_2, t_5):
    '''Returns the value of t_13.'''
    result = t_1 * t_7 + t_2 * t_5
    return result

def t_14(t_1, t_8, t_2, t_6):
    '''Returns the value of t_14.'''
    result = t_1 * t_8 + t_2 * t_6
    return result

def t_15(t_3, t_7, t_4, t_5):
    '''Returns the value of t_15.'''
    result = t_3 * t_7 + t_4 * t_5
    return result

def t_16(t_3, t_8, t_4, t_6):
    '''Returns the value of t_16.'''
    result = t_3 * t_8 + t_4 * t_6
    return result

def t_17(t_13, t_11, t_14, t_9):
    '''Returns the value of t_17.'''
    result = t_13 * t_11 + t_14 * t_9
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

def tan_y(t_19, t_18, t_20):
    '''Returns the value of tan_y.'''
    result = -(t_19 - t_18) / (2. * t_20)
    return result

def tan_x(t_9, t_10, t_11, t_12, tan_y):
    '''Returns the value of tan_x.'''
    result = (t_9 + t_10 * tan_y) / (t_11 + t_12 * tan_y)
    return result

def tan_z(t_5, t_6, t_7, t_8, tan_x):
    '''Returns the value of tan_z.'''
    result = (t_5 + t_6 * tan_x) / (t_7 + t_8 * tan_x)
    return result

def calculate_Vincenty_distance_between_spherical_points(cartesian_array_1,cartesian_array_2,sphere_radius):
    '''Apparently, the special case of the Vincenty formula
	(http://en.wikipedia.org/wiki/Great-circle_distance)
        may be the most accurate method for calculating great-circle distances.'''
    spherical_array_1 = convert_cartesian_array_to_spherical_array(cartesian_array_1)
    spherical_array_2 = convert_cartesian_array_to_spherical_array(cartesian_array_2)
    lambda_1 = spherical_array_1[1]
    lambda_2 = spherical_array_2[1]
    phi_1 = spherical_array_1[2]
    phi_2 = spherical_array_2[2]
    delta_lambda = abs(lambda_2 - lambda_1)
    delta_phi = abs(phi_2 - phi_1)
    radian_angle = math.atan2( math.sqrt( (math.sin(phi_2)*math.sin(delta_lambda))**2 + (math.sin(phi_1)*math.cos(phi_2) - math.cos(phi_1)*math.sin(phi_2)*math.cos(delta_lambda)  )**2 ),  (math.cos(phi_1) * math.cos(phi_2) + math.sin(phi_1) * math.sin(phi_2) * math.cos(delta_lambda) ) )
    spherical_distance = sphere_radius * radian_angle
    return spherical_distance

def convert_cartesian_array_to_spherical_array(coord_array,angle_measure='radians'):
    '''Take shape (N,3) cartesian coord_array and return an array of the same shape in spherical polar form (r, theta, phi). Based on StackOverflow response: http://stackoverflow.com/a/4116899
    use radians for the angles by default, degrees if angle_measure == 'degrees' '''
    spherical_coord_array = numpy.zeros(coord_array.shape)
    xy = coord_array[...,0]**2 + coord_array[...,1]**2
    spherical_coord_array[...,0] = numpy.sqrt(xy + coord_array[...,2]**2)
    spherical_coord_array[...,1] = numpy.arctan2(coord_array[...,1], coord_array[...,0])
    spherical_coord_array[...,2] = numpy.arccos(coord_array[...,2] / spherical_coord_array[...,0])
    if angle_measure == 'degrees':
        spherical_coord_array[...,1] = numpy.degrees(spherical_coord_array[...,1])
        spherical_coord_array[...,2] = numpy.degrees(spherical_coord_array[...,2])
    return spherical_coord_array

def determine_angles(input_coords, sphere_radius, original_tri_area):
    '''Returns the values of the angles
    x, y, z (for specification of the point
    that splits the triangle into three
    equal area subtriangles)
    based on the Cartesian coords
    of the input spherical triangle.
    '''
    A = input_coords[0,...]
    B = input_coords[1,...]
    C = input_coords[2,...]

    arc_length_A = calculate_Vincenty_distance_between_spherical_points(B, C, sphere_radius)
    arc_length_B = calculate_Vincenty_distance_between_spherical_points(A, C, sphere_radius)
    arc_length_C = calculate_Vincenty_distance_between_spherical_points(A, B, sphere_radius)

    s = 0.5 * (arc_length_A + arc_length_B + arc_length_C)

    subtriangle_area = original_tri_area / 3.

    # use the semiperimeter (s) and arc lengths to solve for the requisite
    # spherical triangle angles based on equations made available at
    # http://mathworld.wolfram.com/SphericalTrigonometry.html
    angle_a = 2. * math.asin(math.sqrt((math.sin(s - arc_length_B) * math.sin(s - arc_length_C)) /
                                       (math.sin(arc_length_B) * math.sin(arc_length_C))))
    angle_b = 2. * math.asin(math.sqrt((math.sin(s - arc_length_A) * math.sin(s - arc_length_C)) /
                                       (math.sin(arc_length_A) * math.sin(arc_length_C))))
    angle_c = 2. * math.asin(math.sqrt((math.sin(s - arc_length_A) * math.sin(s - arc_length_B)) /
                                       (math.sin(arc_length_A) * math.sin(arc_length_B))))

    # calculate all the t term values
    t1 = t_1(angle_c, subtriangle_area)
    t2 = t_2(angle_c, subtriangle_area)
    t3 = t_3(angle_c, arc_length_A, subtriangle_area)
    t4 = t_4(angle_c, arc_length_A, subtriangle_area)
    t5 = t_5(angle_a, subtriangle_area)
    t6 = t_6(angle_a, subtriangle_area)
    t7 = t_7(angle_a, subtriangle_area, arc_length_B)
    t8 = t_8(angle_a, subtriangle_area, arc_length_B)
    t9 = t_9(angle_b, subtriangle_area)
    t10 = t_10(angle_b, subtriangle_area)
    t11 = t_11(angle_b, subtriangle_area, arc_length_C)
    t12 = t_12(angle_b, subtriangle_area, arc_length_C)
    t13 = t_13(t1, t7, t2, t5)
    t14 = t_14(t1, t8, t2, t6)
    t15 = t_15(t3, t7, t4, t5)
    t16 = t_16(t3, t8, t4, t6)
    t17 = t_17(t13, t11, t14, t9)
    t18 = t_18(t13, t12, t14, t10)
    t19 = t_19(t15, t11, t16, t9)
    t20 = t_20(t15, t12, t16, t10)

    # finally, calculate the values of x, y, z
    tany = tan_y(t19, t18, t20)
    tanx = tan_x(t9, t10, t11, t12, tany)
    tanz = tan_z(t5, t6, t7, t8, tanx)

    y = math.atan2(tany)
    x = math.atan2(tanx)
    z = math.atan2(tanz)
    return (x, y, z)

def determine_center_point_angles(x,y,z,
                                  original_tri_area,
                                  a,b,c,
                                  sphere_radius):
    '''Determine the angles u,v,w around the desired
    center point D that splits the spherical triangle
    into three equal area subtriangles.'''
    u = (original_tri_area / (3. * sphere_radius ** 2.)) + math.pi - \
        y - c + z
    v = (original_tri_area / (3. * sphere_radius ** 2.)) + math.pi - \
        a + x - z
    w = (original_tri_area / (3. * sphere_radius ** 2.)) + math.pi - \
        x - b + y
    return (u,v,w)
