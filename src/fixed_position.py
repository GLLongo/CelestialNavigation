from position import Position
from skyfield.units import Angle
from skyfield.timelib import Time
from reading import Reading
from geocentric_vector import GeocentricVector
import math



# calculated position of me from several star readings
# (for now we need three readings - in the future i would like to only need two if the hemisphere or general area is known)
class FixedPosition(Position):
    gha: Angle
    des: Angle
    time: Time

    def __init__(self, time: Time) -> None:
        self.gha = None
        self.des = None
        self.time = time

    # returns our calculated position in lat long format calculated from two or more star readings
    def calculate_fixed_position(self, readings: list[Reading]) -> None:
        """
        calculating the intersection of circles on earths surface is equivalent to calculating the intersection of sphers
        with the same center points and with the earth as one of the spheres

        mathematics steps:
        let p_i be the ground_point of reading star i, and let alpha_i be the angle distance away the LOP is from p_i
        1. find the radius of the sphere with center p_i
            1.1. find p_i' : some point on the LOP calculated from star i.
                - we use the point directly north of p_i: p_i'.dec p_i.dec + alpha_i
            1.2 convert p_i and p_i' to cartesian geocentric coordinates (x_i,y_i,z_i) - (earth_center = (0,0,0), 1 unit = radius of earth)
            1.3 find radius r_i of the sphere around p_i = distance between p_i and p_i' (note this is not equivalent to alpha_i)
                - r_i = sqrt((x_i-x_i')^2 + (y_i-y_i')^2 + (z_i-z_i')^2)

        2. find the intersections of the circles
            --calculate the radical line (this will be a plane since we are in 3d) of the first two spheres
            

        :param readings:
        :return: lat long format of our fixed position
        """

        p_geocentric_array=[]
        r_array=[]
        for reading in readings:

            p = reading.body.ground_position()
            alpha = Angle(degrees=90-p.dec.degrees)

            dec_of_prime = p.dec.degrees+alpha.degrees
            if ( dec_of_prime > 360):
                dec_of_prime = dec_of_prime-360
            p_prime = Position(p.gha,Angle(dec_of_prime))

            p_geocentric = GeocentricVector(p)
            p_prime_geocentric = GeocentricVector(p_prime)

            r = p_geocentric.euclidean_distance(p_prime_geocentric) #radius of the sphere centered at p_i

            p_geocentric_array.append(p_geocentric)
            r_array.append(r)

        earth_p = GeocentricVector(0, 0, 0)

        p_0 = p_geocentric_array[0] #first sphere
        r_0 = r_array[0] #first sphere radius

        d_earth_p0 = earth_p.euclidean_distance(p_0) #distance between earth center and sphere 0 center


        #TODO maybe put these calculations into a sphere class
            # with method like - calculate point of intersection, calculate_radius of intersection circle, etc


        #TODO put these calculation withing a sphere or circle class
        #calculate the radius of the intersection circle (intersection of earth and sphere 0)
        under_the_root = 4(d_earth_p0**2) - ((d_earth_p0*2)-(r_0**2))**2 # I_r = 1/2d(4d^2r_1^2-(d^2-r_2^2r_1^2)^2) -- herer r_1 = 1
        intersection1_r = (1/2*d_earth_p0)*math.sqrt(under_the_root)

        #calculate the center of the intersection circle (intersection of earth of sphere 0)
        distance_from_earth_center_to_intersection = math.sqrt(1 + intersection1_r**2) # d^2 = r_1^2 + I_r^2 -- here r_1 = 1
        unit_vector = p_0.unit_vector() #unit vector in direction of p_0 from earth center (0,0,0)

        intersection1_p = unit_vector.times(distance_from_earth_center_to_intersection)



        #intersection circle 2 #TODO we should definitly have a class for this stuff
        p_1 = p_geocentric_array[1]  # first sphere
        r_1 = r_array[1]  # first sphere radius

        d_earth_p1 = earth_p.euclidean_distance(p_1)  # distance between earth center and sphere 1 center


        under_the_root = 4(d_earth_p1 ** 2) - (
                    (d_earth_p1 * 2) - (r_1 ** 2)) ** 2  # I_r = 1/2d(4d^2r_1^2-(d^2-r_2^2r_1^2)^2) -- herer r_1 = 1
        intersection2_r = (1 / 2 * d_earth_p1) * math.sqrt(under_the_root)

        # calculate the center of the intersection circle (intersection of earth of sphere 0)
        distance_from_earth_center_to_intersection = math.sqrt(
            1 + intersection2_r ** 2)  # d^2 = r_1^2 + I_r^2 -- here r_1 = 1
        unit_vector = p_1.unit_vector()  # unit vector in direction of p_0 from earth center (0,0,0)

        intersection2_p = unit_vector.times(distance_from_earth_center_to_intersection)

        #TODO find orientation of these circles: perpendiculat to the unit vector
            #find intersection of these two circles


            #------------
            #find circle at the intersection of one of the spheres and earth
                # - radius
                # -center
                # - orientation of intersecting circle?
            #find circel at the intersection of the other sphere and earth- should be perpendicular to the distance vector between the centers
            #find intersection of the two resultsing circles
            #----------
            # we can use the distance the between the center points and the radius of the circles,
                # then we find the point along the line connecting the two point -- use a vector

            #given a vector (defined by two points) find a point along that line d_1 distance from the first point,m
            


        pass

    def __str__(self) -> None:
        # TODO
        print(self.dec.dms())
