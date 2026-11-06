# Warming-Beam scheme for solving the advection equation
# Authors: Hilary Weller <h.weller@reading.ac.uk>, William Jones <w.j.jones@pgr.reading.ac.uk>

import numpy as np

def warmingBeam(phiLevels, c):
    '''
    Author: William Jones <w.j.jones@pgr.reading.ac.uk>
    Solves the linear advection equation for one time step using Warming and Beam.
    phiLevels is updated. Nothing is returned
    Parameters:
        phiLevels ([1darray]): A list length one containing a 1darray which is
                         the latest value of phi, to be updated.
        c (float): The Courant number
    Returns:
        None
    '''
    # add another time level to the list, copying from the most recent
    phiLevels.append(phiLevels[-1].copy())
    # Labels for phi at time levels n and n+1
    phiOld = phiLevels[0]
    phiNew = phiLevels[1]
    
    # Update phi for all points
    nx = len(phiOld)
    for i in range(nx):
        p1 = 3*phiOld[i] - 4*phiOld[(i-1)%nx] + phiOld[(i-2)%nx]
        p2 = phiOld[i] - 2*phiOld[(i-1)%nx] + phiOld[(i-2)%nx]
        phiNew[i] = phiOld[i] - 0.5*c*p1 + (0.5*c**2)*p2
    
    # Remove the old value of phi
    phiLevels.pop(0)
    return None

