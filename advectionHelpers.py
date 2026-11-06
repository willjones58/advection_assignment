# Helper functions for testing advection schemes.
# Authors: Hilary Weller <h.weller@reading.ac.uk>, William Jones <w.j.jones@pgr.reading.ac.uk>

import numpy as np

def cosBell(x, a, b):
    '''
    Returns a cosine bell shape between parameters a and b
    Author: Hilary Weller <h.weller@reading.ac.uk>
    Parameters:
        x (1darray): The x-locations for calculating the cosine bell.
        a (float): The start of the non-zero bell
        b (float): The end of the non-zero bell
    Returns:
        phi : 1darray. A cosine bell shape between x=a and x=b
    '''
    return np.where((x > a) & (x < b), 
                    0.5*(1 - np.cos(2*np.pi*(x - a)/(b-a))), 0.)
    
def square(x, a, b):
    '''
    Returns a square function with amplitude 1 between parameters a and b, zero elsewhere
    Author: William Jones <w.j.jones@pgr.reading.ac.uk>
    Parameters:
        x (1darray): The x-locations for calculating the square wave.
        a (float): The start of the sqaure wave
        b (float): The end of the sqaure wave
    Returns:
        phi : 1darray. A square wave between x=a and x=b
    '''
    return np.where((x >= a) & (x < b), 1., 0.)

def sine_05(x):
    '''
    Returns a sine wave with amplitude 1 and period 1, centered at the origin.
    Author: William Jones <w.j.jones@pgr.reading.ac.uk>
    Parameters:
        x (1darray): The x-locations for calculating the sine wave.
    Returns:
        phi : 1darray. A cosine bell shape between x=a and x=b
    '''
    return np.sin(2*np.pi*x)

def square_01_05(x):
    "square initial conditions with a=0.1, b=0.5"
    return square(x, 0.1, 0.5)
    
def cosBell_01_05(x):
    "cosBell initial conditions with a=0.1, b=0.5"
    return cosBell(x, 0.1, 0.5)

def l2error(phi, phiA):
    '''
    Returns the l2 error norm of phi in comparison to exact solution phiA.
    Author: Hilary Weller <h.weller@reading.ac.uk>
    Parameters:
        phi (1darray): The numerical solution
        phiA (1darray): The analytic solution
    Returns
        l2 (float): The l2 error norm
    '''
    phiError = phi - phiA
    l2 = np.sqrt(np.sum(phiError**2)/np.sum(phiA**2))
    return l2
