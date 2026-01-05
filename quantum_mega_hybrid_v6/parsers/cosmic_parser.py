"""Astropy cosmic parser — universe sim"""

from astropy.cosmology import Planck18

def parse_cosmic_expansion(max_z: float = 5.0):
    import numpy as np
    z = np.linspace(0, max_z, 10)
    return Planck18.comoving_distance(z).value.tolist()
