# quantum-wave-packet-simulator

Numerical quantum mechanics using Python, including Gaussian wave packets, finite-difference Hamiltonians, and infinite-well eigenstates.

# Quantum Wave-Packet Simulator

> **Status: Work in progress — numerical foundations implemented**

A Python project exploring one-dimensional quantum mechanics using finite-difference methods, sparse matrices and numerical eigensolvers.

The long-term aim is to simulate the time-dependent Schrödinger equation for Gaussian wave packets interacting with potential wells, steps and barriers, including quantum tunnelling. The current version establishes and validates the numerical foundations needed for that simulation.

## Current implementation

* Construction and normalisation of a complex Gaussian wave packet
* Visualisation of the wavefunction, probability density, real component and imaginary component
* Finite-difference approximation of the second derivative
* Reusable sparse kinetic-energy and Hamiltonian operators
* Numerical solution of the infinite square well eigenvalue problem
* Comparison between numerical and analytical energies
* Numerical normalisation of eigenfunctions
* Comparison between numerical and analytical eigenstates
* Grid-refinement convergence testing
* Numerical confirmation of second-order finite-difference convergence

## Physics

The project uses the one-dimensional Hamiltonian

$$
\hat{H}
=
-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
+
V(x).
$$

The second derivative is approximated using the central-difference expression

$$
\psi''(x_i)
\approx
\frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{(\Delta x)^2}.
$$

For the infinite square well, the numerical solutions are validated against the analytical energies

$$
E_n
=
\frac{n^2\pi^2\hbar^2}{2mL^2}
$$

and eigenfunctions

$$
\psi_n(x)
=
\sqrt{\frac{2}{L}}
\sin\left(\frac{n\pi x}{L}\right).
$$

## Repository contents

* `01_gaussian_packet.ipynb` — constructs and normalises the initial Gaussian wave packet
* `02_infinite_well_eigenstates.ipynb` — solves and validates the infinite-square-well eigenvalue problem
* `hamiltonian.py` — reusable finite-difference kinetic-energy and Hamiltonian operators
* `requirements.txt` — Python dependencies

## Installation

Clone the repository:

```bash
git clone https://github.com/OLIVIA-W1287/quantum-wave-packet-simulator.git
cd quantum-wave-packet-simulator
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter lab
```

The notebooks should be run in numerical order.

## Numerical validation

The infinite-well calculation is checked by:

1. Comparing numerical eigenvalues with exact analytical energies.
2. Comparing numerical and analytical eigenfunctions.
3. Checking wavefunction normalisation.
4. Measuring the convergence rate as the spatial grid is refined.

The measured convergence is approximately second order, consistent with the central-difference discretisation.

## Current limitations

The time-evolution solver has not yet been implemented. The current release focuses on constructing the initial wave packet and validating the spatial Hamiltonian through a stationary-state problem.

## Planned development

* Implement time evolution using Crank–Nicolson or split-step Fourier propagation
* Validate free-particle wave-packet spreading
* Add finite wells, potential steps and finite barriers
* Calculate reflection and transmission probabilities
* Investigate quantum tunnelling
* Add absorbing boundary conditions
* Produce animations of wave-packet evolution

## Technologies

Python, NumPy, SciPy, Matplotlib, Jupyter, sparse matrix methods and finite-difference numerical analysis.
