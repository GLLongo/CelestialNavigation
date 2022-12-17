from celestial_body import CelestialBody
from position import Position
from skyfield.units import Angle
from skyfield.timelib import Time


#ground position of a celestial body
class GroundPosition(Position):
    #TODO type hints of all vars here
    
    def __init__(self, celestial_body: CelestialBody, gha: Angle ,dec: Angle, time: Time) -> None:
        self.CelestialBody = celestial_body
        self.time = time
        super.__init__(dec, gha)

