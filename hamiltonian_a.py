import numpy as np
from scipy.sparse import diags


def kinetic_operator(N, dx, hbar=1.0, m=1.0):
    """
    Constructs the kinetic energy operator using finite difference method.

    Parameters:
    N (int): Number of grid points.
    dx (float): Grid spacing.
    hbar (float): Reduced Planck's constant (default is 1.0).
    m (float): Mass of the particle (default is 1.0).

    Returns:
    scipy.sparse.csr_matrix: Sparse matrix representing the kinetic energy operator T.
    """
    main_diag = -2.0 * np.ones(N)
    off_diag = np.ones(N - 1)

    D2 = diags(
        [off_diag, main_diag, off_diag],
        offsets=[-1, 0, 1]
    ) / dx**2

    T = -(hbar**2) / (2 * m) * D2

    return T


def build_hamiltonian(x, V, hbar=1.0, m=1.0):
    """
    Constructs the 1D finite difference Hamiltonian operator for a given potential V(x).

    Parameters:
    x: array_like
        The interior spatial grid points.
    V: array_like
        The potential energy evaluated at each of the interior grid points.
    hbar: float, optional
        The reduced Planck's constant (default is 1.0).
    m: float, optional
        The mass of the particle (default is 1.0).
    
    Returns:
    H: scipy.sparse matrix
        The Hamiltonian operator as a sparse matrix.
    """

    x = np.asarray(x)
    V = np.asarray(V)

    if len(x) != len(V):
        raise ValueError("x and V must have the same number of elements.")

    if len(x) < 2:
        raise ValueError("x must contain at least two grid points.")

    N = len(x)
    dx = x[1] - x[0]
    T = kinetic_operator(N, dx, hbar=hbar, m=m)
    V_op = diags(V, offsets=0)
    H = T + V_op
    return H