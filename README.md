Advection assignment. William Jones <w.j.jones@pgr.reading.ac.uk>
Code to solve the advection equation.
advectionAssignment.py   : Run this file to produce the results for the advection assignment
advectionSnapshot.py     : Function to save plots of snapshots of the results.
orderOfConvergence.py    : Function to save plots of the l2 error againt the spatial resolution 
                           for multiple functions to visulaise the order of convergence
courantErrors.py         : Functions to save plots of l2 error against courant number,
                           acheived by either varying spatial and temporal resolution.

advectionHelpers.py   : Functions for initialising and calculating l2 error norm
schemesBasic.py    : FTCS, CTCS and FTBS advection schemes
schemeWarmingBeam.py : Warming and Beam advection scheme