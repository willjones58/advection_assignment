###############################################################################
# Date Revised: 6 Nov 2026
# Author: William Jones <w.j.jones@pgr.reading.ac.uk>
# Description: Tests the order of convergence of linear advection schemes
###############################################################################
import matplotlib.pyplot as plt
import numpy as np
from advectionHelpers import l2error

def orderOfConvergence(init, schemes, outFile, nx, ntFactor = 10, u = 1, endTime = 0.4, xLim = [0,1]):
    '''
    Author: William Jones <w.j.jones@pgr.reading.ac.uk>
    Plots the orders of convergence of advection schemes using periodic boundaries
    Parameters:
        init (callable): Function to set the initial conditions.
        schemes (callable): Schemes to evaluate.
        nx (1darray): An array containing the varying numbers of points in space to to be evaluated
        nt_factor (int): The number of times steps for each resolution is given by nt_factor*nx
        u (float): The wind speed
        endTime (float) : The final time
        outFile (string): The name of the output file.
        xLim (tuple): The minimum (xLim[0]) and maximim (xLim[1]) x-values of
                      the domain. xLim[1] is not part of the domain when periodic
    
    Returns:
        None
    '''
    # Colours for each line
    cols = ['#D55E00', '#56B4E9', '#009E73', '#CC79A7', '#E69F00', "#F0E442", '#0072B2']

    # Set nt = A*nx so that the Courant number is fixed.
    nt = ntFactor*nx

    # Derived parameters
    dx = (xLim[1] - xLim[0])/nx # An array of the resolutions
    c = u*endTime/(ntFactor*(xLim[1] - xLim[0])) # Courant number, dt*u/dx. Since nt = nt_factor*nx, nx cancels.
    print('Courant number =', c)
    
    plt.figure()

    for i in range(len(schemes)):
        # Set up an array to store the l2 erorrs for each value of dx
        errors = np.zeros(len(nx))
        
        # Copmute the l2 error for each resolution
        for j in range(len(nx)):
            
            # Values of x for the current resolution
            x = np.linspace(xLim[0], xLim[1], nx[j], endpoint=False)

            # Set the initial conditions
            phi0 = init(x)
        
            # Find the analytic solution
            phiA = init((x - u*endTime)%(xLim[1] - xLim[0]))
            
            # The solution, phi, is stored as a list of arrays at different time
            # steps, phiLevels. Initially just the initial conditions. The latest
            # time level array is always phiLevels[-1]
            phiLevels = [phi0.copy()]
            for n in range(nt[j]):
                schemes[i](phiLevels, c)
            
            # Calculate the error for this resolution and store it in the errors array
            errors[j] = l2error(phiLevels[-1], phiA)

        plt.loglog(dx, errors, 'o-', c = cols[i], linewidth=1.25, markersize=2, label = schemes[i].__name__)

    plt.loglog(dx,10*dx**2, '--', linewidth = 1, c = "#414141", label = r'$\ell_2 = \mathcal{O}(\Delta x^2)$')
    plt.loglog(dx,10*dx, ':', linewidth = 1, c = "#414141", label = r'$\ell_2 = \mathcal{O}(\Delta x)$')
    plt.grid(which = "both")
    plt.xlabel(r'$\Delta x$')
    plt.ylabel(r'$\ell_2$')
    plt.legend()
    plt.savefig("plots/"+outFile)

# Can we plot the order of convergence, for varying values of c on one graph for warming beam, so nt_factor is variable