"""HUX-f and HUX-b propagation implemented. """
import numpy as np
import scipy


def apply_hux_f_model(r_initial, dr_vec, dp_vec, r0=30 * 695700, alpha=0.15, rh=50 * 695700, add_v_acc=True,
                      omega_rot=(2 * np.pi) / (25.38 * 86400)):
    """Apply 1d upwind model to the inviscid burgers equation.
    r/phi grid. return and save all radial velocity slices.

    :param r_initial: 1d array, initial condition (vr0). units = (km/sec).
    :param dr_vec: 1d array, mesh spacing in r. units = (km)
    :param dp_vec: 1d array, mesh spacing in p. units = (radians)
    :param alpha: float, hyper parameter for acceleration (default = 0.15).
    :param rh: float, hyper parameter for acceleration (default r=50*695700). units: (km)
    :param r0: float, initial radial location. units = (km).
    :param add_v_acc: bool, True will add acceleration boost.
    :param omega_rot: differential rotation.
    :return: velocity matrix dimensions (nr x np)
    """
    v = np.zeros((len(dr_vec) + 1, len(dp_vec) + 1))  # initialize array vr.
    v[0, :] = r_initial

    if add_v_acc:
        v_acc = alpha * (v[0, :] * (1 - np.exp(-r0 / rh)))
        v[0, :] = v_acc + v[0, :]

    for i in range(len(dr_vec)):
        for j in range(len(dp_vec) + 1):

            if j == len(dp_vec):  # force periodicity
                v[i + 1, j] = v[i + 1, 0]

            else:
                if (omega_rot * dr_vec[i]) / (dp_vec[j] * v[i, j]) > 1:
                    print(dr_vec[i] - dp_vec[j] * v[i, j] / omega_rot)
                    print(i, j)  # courant condition

                frac1 = (v[i, j + 1] - v[i, j]) / v[i, j]
                frac2 = (omega_rot * dr_vec[i]) / dp_vec[j]
                v[i + 1, j] = v[i, j] + frac1 * frac2

    return v


def apply_hux_b_model(r_final, dr_vec, dp_vec, alpha=0.15, rh=50 * 695700, add_v_acc=True,
                      r0=30 * 695700, omega_rot=(2 * np.pi) / (25.38 * 86400)):
    """ Apply 1d backwards propagation.

    :param r_final: 1d array, initial velocity for backward propagation. units = (km/sec).
    :param dr_vec: 1d array, mesh spacing in r.
    :param dp_vec: 1d array, mesh spacing in p.
    :param alpha: float, hyper parameter for acceleration (default = 0.15).
    :param rh:  float, hyper parameter for acceleration (default r=50 rs). units: (km)
    :param add_v_acc: bool, True will add acceleration boost.
    :param r0: float, initial radial location. units = (km).
    :param omega_rot: differential rotation.
    :return: velocity matrix dimensions (nr x np) """

    v = np.zeros((len(dr_vec) + 1, len(dp_vec) + 1))  # initialize array vr.
    v[-1, :] = r_final

    for i in range(len(dr_vec)):
        for j in range(len(dp_vec) + 1):

            if j != len(dp_vec):
                # courant condition
                if (omega_rot * dr_vec[i]) / (dp_vec[j] * v[-(i + 1), j]) > 1:
                    print("CFL violated", dr_vec[i] - dp_vec[j] * v[-(i + 1), j] / omega_rot)
                    raise ValueError('CFL violated')

                frac2 = (omega_rot * dr_vec[i]) / dp_vec[j]
            else:
                frac2 = (omega_rot * dr_vec[i]) / dp_vec[0]

            frac1 = (v[-(i + 1), j - 1] - v[-(i + 1), j]) / v[-(i + 1), j]
            v[-(i + 2), j] = v[-(i + 1), j] + frac1 * frac2

    # add acceleration after upwind.
    if add_v_acc:
        v_acc = alpha * (v[0, :] * (1 - np.exp(-r0 / rh)))
        v[0, :] = -v_acc + v[0, :]

    return v


def apply_forward_upwind_model(r_initial, dr_vec, dp_vec, alpha=0.15, rh=50 * 695700, add_v_acc=True, r0=30 * 695700,
                               omega_rot=(2 * np.pi) / (25.38 * 86400)):
    """ Apply 1d forward upwind model. r/phi grid.

    :param r_initial: 1d array, initial condition (vr0). units = (km/sec).
    :param dr_vec: 1d array, mesh spacing in r.
    :param dp_vec: 1d array, mesh spacing in p.
    :param alpha: float, hyper parameter for acceleration (default = 0.15).
    :param rh:  float, hyper parameter for acceleration (default r=50 rs). units: (km)
    :param add_v_acc: bool, True will add acceleration boost.
    :param r0: float, initial radial location. units = (km).
    :param omega_rot: differential rotation.
    :return: vr at r end.
    """
    v_next = np.zeros(len(dp_vec) + 1)  # initialize v_next.
    v_prev = r_initial

    # add acceleration before upwind.
    if add_v_acc:
        v_acc = alpha * (v_prev * (1 - np.exp(-r0 / rh)))
        v_prev = v_acc + v_prev

    for i in range(len(dr_vec)):
        for j in range(len(dp_vec) + 1):

            if j == len(dp_vec):  # force periodicity
                v_next[-1] = v_next[0]

            else:
                # courant condition
                if (omega_rot * dr_vec[i]) / (dp_vec[j] * v_prev[j]) > 1:
                    print("CFL violated", dr_vec[i] - dp_vec[j] * v_prev[j] / omega_rot)
                    raise ValueError('CFL violated')

                frac1 = (v_prev[j + 1] - v_prev[j]) / v_prev[j]
                frac2 = (omega_rot * dr_vec[i]) / dp_vec[j]
                v_next[j] = v_prev[j] + frac1 * frac2

        # update v_prev to be the current v. np.copy- deep copy so when we modify
        # v_next v_prev does not change.
        v_prev = np.copy(v_next)

    return v_next


def apply_backwards_upwind_model(r_final, dr_vec, dp_vec, alpha=0.15, rh=50 * 695700, add_v_acc=True,
                                 r0=30 * 695700, omega_rot=(2 * np.pi) / (25.38 * 86400)):
    """ Apply 1d backwards upwind model to the inviscid burgers equation. r/phi grid.

    :param r_final: 1d array, initial velocity for backward propagation. units = (km/sec).
    :param dr_vec: 1d array, mesh spacing in r.
    :param dp_vec: 1d array, mesh spacing in p.
    :param alpha: float, hyper parameter for acceleration (default = 0.15).
    :param rh:  float, hyper parameter for acceleration (default r=50 rs). units: (km)
    :param add_v_acc: bool, True will add acceleration boost.
    :param r0: float, initial radial location. units = (km).
    :param omega_rot: differential rotation.
    :return: vr at r0. """

    v_next = np.zeros(len(dp_vec) + 1)  # initialize v_next.
    v_prev = r_final  # v_previous, r = 1 AU.

    for i in range(len(dr_vec)):
        for j in range(len(dp_vec) + 1):

            if j != len(dp_vec):
                # courant condition
                if (omega_rot * dr_vec[i]) / (dp_vec[j] * v_prev[j]) > 1:
                    print("CFL violated", dr_vec[i] - dp_vec[j] * v_prev[j] / omega_rot)
                    raise ValueError('CFL violated')

                frac2 = (omega_rot * dr_vec[i]) / dp_vec[j]
            else:
                frac2 = (omega_rot * dr_vec[i]) / dp_vec[0]

            frac1 = (v_prev[j - 1] - v_prev[j]) / v_prev[j]
            v_next[j] = v_prev[j] + frac1 * frac2

        # update v_prev to be the current v. np.copy- deep copy so when we modify
        # v_next v_prev does not change.
        v_prev = np.copy(v_next)

    # add acceleration after upwind.
    if add_v_acc:
        v_acc = alpha * (v_next * (1 - np.exp(-r0 / rh)))
        v_next = -v_acc + v_next

    return v_next


def apply_ballistic_approximation(v_initial, dr, phi_vec, omega_rot=(2 * np.pi) / (25.38 * 86400)):
    """ Apply the ballistic model for mapping solar wind streams to
    different locations in the heliosphere is the simplest possible approximation

    :param phi_vec: mesh carrington longitude spacing (radians).
    :param v_initial: 1d array, initial velocity for ballistic. units = (km/sec).
    :param dr: delta r. units = (km).
    :param omega_rot: differential rotation. (1/secs)
    :return: shifted phi coordinates. """

    # delta_phi = -omega * delta_r / (vr0)
    delta_phi = (omega_rot * dr)/v_initial
    phi_shifted = phi_vec - delta_phi
    # force periodicity
    return phi_shifted % (2*np.pi)



