#!/usr/bin/env python3

from numpy import linspace, log, sqrt, array, empty, savetxt
from pylab import plot, show

# init output array
n = 100
dat = empty([n, 14])

# distance from vessel
x = linspace(0, 1, n)
dat[:,0] = x

# resource density
L = 1
rmax = 1
#def r(x):
#    x = L - x
#    return(rmax * x / L)
def r(x):
	x = 0.01**x
	return(rmax*x)
dens = r(x)
dat[:,1] = dens

# no investment
c = 0.9
dr = linspace(0, 0, 100)
resources = dens
cost = c * dr
mumax = 1
k = 0.5
def mu(r):
    y = r + k
    return(mumax * r / y)
growth = mu(dens)
effgrowth = growth - cost

dat[:,2] = dr
dat[:,3] = resources
dat[:,4] = growth
dat[:,5] = effgrowth

# constitutive investment
dr = sqrt(k / c) - k
resources = dens + dr
cost = c * dr
growth = mu(resources)
effgrowth = growth - cost

dat[:,6] = dr
dat[:,7] = resources
dat[:,8] = growth
dat[:,9] = effgrowth

# responsive investment
dr = sqrt(k / c) - k - dens
# replace all negative values with zero
dr = array([ max(0, i) for i in dr ])
resources = dens + dr
cost = c * dr
growth = mu(resources)
effgrowth = growth - cost

dat[:,10] = dr
dat[:,11] = resources
dat[:,12] = growth
dat[:,13] = effgrowth

# save dat
savetxt("exponential.csv", dat, delimiter=",")
