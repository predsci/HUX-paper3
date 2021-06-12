import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def compute_phi_shift_forward(p, r, v, omega=(2 * np.pi) / (25.38 * 86400)):
    # initialize phi shift matrix.
    phi_shift_vec = np.zeros(len(r))

    # phi at index 0 is original phi grid
    phi_shift_vec[0] = p

    # delta r.
    dr = np.mean(r[1:] - r[:-1])

    # compute the phi shift for each idx in r.
    for ii in range(0, len(r) - 1):
        phi_shift = -(omega / v) * dr
        phi_shift_vec[ii + 1] = phi_shift_vec[ii] + phi_shift

    return phi_shift_vec


def cmap_spiral(nphi):
    # an array of parameters, each of our curves depend on a specific value of parameters.
    parameters = np.linspace(0, 2*np.pi, nphi)
    # norm is a class which, when called, can normalize data into the [0.0, 1.0] interval.
    norm = mpl.colors.Normalize(vmin=np.min(parameters), vmax=np.max(parameters))
    # create a ScalarMappable and initialize a data structure
    arr = mpl.cm.ScalarMappable(cmap=mpl.cm.hsv, norm=norm)
    arr.set_array([])
    return arr