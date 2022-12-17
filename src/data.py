#this module holds all data and global variables becuase i dont know how to use python correctly
from skyfield.api import Star, load
from skyfield.data import hipparcos
from skyfield.timelib import Time, Timescale
from skyfield.vectorlib import VectorSum
from skyfield.jpllib import SpiceKernel
import pandas as pd

planets: SpiceKernel
earth: VectorSum
ts: Timescale
hip: pd.DataFrame
hip_navigational_stars: pd.DataFrame


def init(self):

    global planets
    global ts
    global hip
    global earth
    global hip_navigational_stars

    planets = load('de421.bsp')
    earth = planets['earth']

    ts = load.timescale()
    with load.open(hipparcos.URL) as f:
         hip = hipparcos.load_dataframe(f)

    hip_navigational_stars = hip[hip['magnitude'] <= 2.5] #TODO later this should only be the navigational stars in the nautical almanac, right now im just using the brightest cuz its easy


