from skyfield.units import Angle
from position import Position
import math
from __future__ import annotations


class GeocentricVector:
    x: float
    y: float
    z: float

    def __init__(self, position: Position):
        self.x = math.cos(position.dec.radians) * math.cos(position.gha.radians)
        self.y = math.cos(position.dec.radians) * math.sin(position.gha.radians)
        self.z = math.sin(position.dec.radians)
        pass



    def __init__(self,x:float,y:float,z:float):
        self.x = x
        self.y = y
        self.z = z

    #retuns the euclidean distance between self and geo_position
    def euclidean_distance(self,geo_position: GeocentricVector) -> float:
        return math.sqrt((self.x - geo_position.x)**2 + (self.y - geo_position.y)**2 + (self.z - geo_position.z)**2)

    def magnitude(self) -> float:
        return self.euclidean_distance(GeocentricVector(0,0,0))

    def unit_vector(self) -> GeocentricVector:
        #find the unit vector in the same direction of this vector
        mag = self.magnitude()
        return GeocentricVector(self.x/mag, self.y/mag, self.z/mag)


    #return new vector = this multiplies by scaler s
    def times(self,s:float) -> GeocentricVector:
        return GeocentricVector(self.x*s,self.y*s,self.z*s)

    #returns the cross product of self and vector v
    def cross_product(self, v: 'GeocentricVector'):
        #TODO
        pass

    #returns new vector equal to self - v
    def minus(self, v: 'GeocentricVector') -> 'GeocentricVector':
        return(GeocentricVector(self.x - v.x,self.y - v.y,self.z-v.z))
