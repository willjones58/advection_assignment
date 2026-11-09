###############################################################################
# Date Revised: 6 Nov 2025
# Author: William Jones <w.j.jones@pgr.reading.ac.uk>
# Description: Test the order of convergence of Linear advection schemes
###############################################################################
import matplotlib.pyplot as plt
import numpy as np
from advectionHelpers import l2error

def courantErrorsDt(init, schemes, outFile, nt,
                           nx = 40, u = 1, endTime = 0.4,
                           xLim = [0,1], yLim = [None,None]):
    '''
    Author: William Jones <w.j.jones@pgr.reading.ac.uk>
    Evaluates the l2 error of multiple advection schemes for varying Courant numbers by varying nt, with nx constant
    Parameters:
        nx (int): The numbers of points in space.
        init (callable): Function to set the initial conditions.
        schemes (callable): Schemes to evaluate.
        nt (1darray): An array containing the different numbers of time steps.
        u (float): The wind speed
        endTime (float) : The final time
        outFile (string): The name of the output file.
        xLim (tuple): The minimum (xLim[0]) and maximim (xLim[1]) x-values of
                      the domain. xLim[1] is not part of the domain when periodic
        yLim (tuple): The minimum (yLim[0]) and maximum (yLim[1]) y values of
                      the graph. If [None,None] is specified then default limits
                      are used.
    Returns:
        None
    '''
    
    # Derived parameters
    dx = (xLim[1] - xLim[0])/nx
    c = nx*u*endTime/(nt*(xLim[1] - xLim[0])) # Courant numbers, dt*u/dx
    x = np.linspace(xLim[0], xLim[1], nx, endpoint=False)
            
    # Set the initial conditions
    phi0 = init(x)
        
    # Find the analytic solution
    phiA = init((x - u*endTime)%(xLim[1] - xLim[0]))
    
    # Colours for each line
    cols = ['#D55E00', '#56B4E9', '#009E73', '#CC79A7', '#E69F00', "#F0E442", '#0072B2']
    
    plt.figure()
    
    for i in range(len(schemes)):
        # Set up an array to store the l2 erorrs for each resolution
        errors = np.zeros(len(nt))

        # Evaluate the numerical scheme for each value of nt
        for j in range(len(nt)):
            
            # The solution, phi, is stored as a list of arrays at different time
            # steps, phiLevels. Initially just the initial conditions. The latest
            # time level array is always phiLevels[-1]
            phiLevels = [phi0.copy()]
            for n in range(nt[j]):
                schemes[i](phiLevels, c[j])
            
            # Calculate the error for this courant number and store it in the errors array
            errors[j] = l2error(phiLevels[-1], phiA)
        
        plt.semilogy(c, errors, cols[i], label = schemes[i].__name__)

    plt.ylim(yLim)
    plt.xlabel(r'$c$')
    plt.ylabel(r'$\ell_2$')
    plt.grid(which='both')
    plt.legend()
    plt.savefig("plots/"+outFile)

def courantErrorsDx(init, schemes, outFile,
                           nx, nt = 10, u = 1, endTime = 0.4,
                           xLim = [0,1], yLim = [None,None]):
    '''
    Author: William Jones <w.j.jones@pgr.reading.ac.uk>
    Evaluates the l2 error of multiple advection schemes for varying Courant numbers by varying nx, with nt constant
    Parameters:
        nx (1darray): An array containing the numbers of points in space.
        init (callable): Function to set the initial conditions.
        schemes (callable): Schemes to evaluate.
        nt (int): The number of time steps.
        u (float): The wind speed
        endTime (float) : The final time
        outFile (string): The name of the output file.
        xLim (tuple): The minimum (xLim[0]) and maximim (xLim[1]) x-values of
                      the domain. xLim[1] is not part of the domain when periodic
        yLim (tuple): The minimum (yLim[0]) and maximum (yLim[1]) y values of
                      the graph. If [None,None] is specified then default limits
                      are used.
    Returns:
        None
    '''
    # Derived parameters
    dx = (xLim[1] - xLim[0])/nx
    c = nx*u*endTime/(nt*(xLim[1] - xLim[0])) # Courant numbers, dt*u/dx
    
    # Colours for each line
    cols = ['#D55E00', '#56B4E9', '#009E73', '#CC79A7', '#E69F00', "#F0E442", '#0072B2']
    
    plt.figure()
    
    for i in range(len(schemes)):
        # Set up an array to store the l2 erorrs for each resolution
        errors = np.zeros(len(nx))

        # Evaluate the numerical scheme for each value of nx
        for j in range(len(nx)):
            
            # Calculate the grid points for the current number of points in space
            x = np.linspace(xLim[0], xLim[1], nx[j], endpoint=False)
            
            # Set the initial conditions
            phi0 = init(x)
        
            # Find the analytic solution
            phiA = init((x - u*endTime)%(xLim[1] - xLim[0]))
            
            # The solution, phi, is stored as a list of arrays at different time
            # steps, phiLevels. Initially just the initial conditions. The latest
            # time level array is always phiLevels[-1]
            phiLevels = [phi0.copy()]
            for n in range(nt):
                schemes[i](phiLevels, c[j])
            
            # Calculate the error for this courant number and store it in the errors array
            errors[j] = l2error(phiLevels[-1], phiA)
        
        plt.semilogy(c, errors, cols[i], label = schemes[i].__name__)

    plt.ylim(yLim)
    plt.xlabel(r'$c$')
    plt.ylabel(r'$\ell_2$')
    plt.grid(which='both')
    plt.legend()
    plt.savefig("plots/"+outFile)