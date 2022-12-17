# TODO how do i make classes abstract?
from skyfield.units import Angle


class Position(object):
    # TODO type hints of all vars here
    def __init__(self,gha: Angle,dec: Angle) -> None:
        self.dec = dec
        self.gha = gha

    def __str__(self) -> str:
        #TODO
        return self.dec + " " + self.gha #TODO make this output how it is formally writen

