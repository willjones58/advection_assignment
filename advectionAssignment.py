###############################################################################
# Date Revised: 9 Nov 2026
# Authors: William Jones <w.j.jones@pgr.reading.ac.uk>, Hilary Weller <h.weller@reading.ac.uk
# Description: Produces results for the advection asignment
###############################################################################
import matplotlib.pyplot as plt
import numpy as np
import os
from advectionSnapshots import compareSchemeSnapshots
from orderOfConvergence import orderOfConvergence
from courantErrors import courantErrorsDt, courantErrorsDx
from advectionHelpers import cosBell_01_05, square_01_05, sine_05
from schemesBasic import FTBS, CTCS, FTCS
from schemeWarmingBeam import warmingBeam

# First make sure that the plots folder exists
if not os.path.exists("plots"):
    os.makedirs("plots")

# Lists of functions to do the advection
schemesBasic = [FTBS, CTCS, FTCS]
schemesAlt = [FTBS, CTCS, warmingBeam]

###############################################################################
# Section 3
# Produce snapshots of the numerical solutions to the linear advection solution for schemesBasic, c = 0.4

compareSchemeSnapshots(cosBell_01_05, schemesBasic, "basicSchemesCos.pdf",
                        nx = 40, nt = 10, u = 1, endTime = 0.1, xLim = [0,1])

compareSchemeSnapshots(square_01_05, schemesBasic, "basicSchemesSquare.pdf",
                        nx = 40, nt = 10, u = 1, endTime = 0.1, xLim = [0,1])

###############################################################################
# Section 5.1
# Produce snapshots of the numerical solutions to the linear advection solution for schemesAlt, c = 0.4

compareSchemeSnapshots(cosBell_01_05, schemesAlt, "warmingBeamCos.pdf",
                        nx = 40, nt = 10, u = 1, endTime = 0.1, xLim = [0,1])

compareSchemeSnapshots(square_01_05, schemesAlt, "warmingBeamSquare.pdf",
                        nx = 40, nt = 10, u = 1, endTime = 0.1, xLim = [0,1])

###############################################################################
# Section 5.2
# Plot the order of convergence

# 10 integers that are approximately evenly spaced on the log-scale, in the interval [10,100]
nx = np.array([10**(1+0.1*i) for i in range(11)], dtype = int)

orderOfConvergence(sine_05, schemesAlt, "orderOfConvergence.pdf", nx = nx, ntFactor=10, u = 1, endTime = 0.4, xLim = [0,1])

###############################################################################
# Section 5.3
# Plot the error against c

# Values of nt that give Courant numbers approximately equal to the series (0.1,0.2,...,2.3)
nt = np.array([40/(0.1*i) for i in range(1,24)], dtype = int)

courantErrorsDt(cosBell_01_05, schemesAlt, "courantErrorsDt.pdf", nt = nt, nx = 100, u = 1, endTime = 0.4, xLim = [0,1], yLim = [10**-3,10])

# Values of nx that give Courant numbers exactly equal to the series (0.1,0.2,...,2.3)
nx =  np.arange(50,1150,50)

courantErrorsDx(cosBell_01_05, schemesAlt, "courantErrorsDx.pdf", nx = nx, nt = 200, u = 1, endTime = 0.4, xLim = [0,1], yLim = [10**-5,10])
