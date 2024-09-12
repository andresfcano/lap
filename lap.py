#!/usr/bin/env python3
"""
   Computes a (regularized) solution to the linear assignment
   problem by the Sinkhorn algorithm.
   
   (C) Michele Ceriotti 2015
"""

import numpy as np
import sys
import time


def sinkhorn(m, g, eps=1e-9):
    n = len(m)
    l = 1 / (g * m.sum() / (n * n))
    mx = m.max()
    k = np.exp((m - mx) * l)
    e = np.ones(n)
    v = np.ones(n)
    u = np.ones(n)

    while ((u * np.dot(k, v) - e)**2).sum() > eps:
        u = e / np.dot(k, v)
        v = e / np.dot(u, k)

    for i in range(n):
        k[i, :] *= u[i] * v

    w = np.sum(k * m)

    return w, k


def main(mtx, gamma=1e-2):
    """ 
    mtx: filename for input data
    gamma: regularization parameter for sinkhorn algorithm
    """

    cij = np.loadtxt(mtx)
    
    # Start the timer
    start_time = time.time()

    w, p = sinkhorn(cij, gamma)

    # Stop the timer
    end_time = time.time()
    # Calculate the duration
    duration = end_time - start_time
    print(f"Time taken: {duration:.4f} seconds")

    print(f"Regularized LAP result (rounded): {np.round(w):.0f}")
    np.savetxt(fname="lap.dat",
               X=p,
               header=f"Regularized LAP result: {w}",
               fmt="%10.5e")

if __name__ == '__main__':
    main(*sys.argv[1:])
