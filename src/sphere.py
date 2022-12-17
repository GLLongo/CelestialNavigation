from circle_3D import Circle3D
from geocentric_vector import GeocentricVector
import math

class Sphere:
    center: GeocentricVector
    radius: float

    def __init__(self, center: GeocentricVector, radius: float) -> None:
        self.center = center
        self.radius = radius


    #calculates the intersection of these sphere and earth (earth is located at (0,0,0) with a radius of 1)
    def find_intersection_with_earth(self) -> Circle3D:
        # calculate the radius of the intersection circle (intersection of earth and sphere 0)

        earth = Sphere(GeocentricVector(0, 0, 0), 1)

        distance = self.euclidean_distance(earth) #distance between earth center and sphere 0 center
        under_the_root = 4(distance ** 2) -((distance * 2) - (self.radius ** 2)) ** 2

        #radius of intersecting circle
        r = (1 / 2 * distance) * math.sqrt(under_the_root)

        # calculate the center of the intersection circle (intersection of earth of sphere 0)
        distance_from_earth_center_to_intersection = math.sqrt(1 + r ** 2)  # d^2 = r_1^2 + I_r^2 -- here r_1 = 1
        unit_vector = self.center.unit_vector()  # unit vector in direction of self.center from earth center (0,0,0)

        p = unit_vector.times(distance_from_earth_center_to_intersection)

        #since the circle les perpenducular to the line between the centers of the two spheres we the nromal vector is the same as this line
        # this line can be defined using just the center of self.sphere since the other point on the line is (0,0,0)

        intersectionCircle = Circle3D(p, r, self.center)


    #returns the euclidean distnace between centers of self and sphere
    def distance(self, sphere: 'Sphere') -> float:
        return self.center.euclidean_distance(sphere.center)
