import numpy as np
from qiskit.quantum_info import Operator

# toy phonon
def truncated_oscillator_hamiltonian(n_levels=4, omega=1.0):
    # Creation and annihilation operators in truncated basis
    a = np.zeros((n_levels, n_levels), dtype=complex)
    for n in range(1, n_levels):
        a[n-1, n] = np.sqrt(n)
    adag = a.conj().T
    
    H = omega * (adag @ a + 0.5 * np.eye(n_levels))
    return H

H_osc = truncated_oscillator_hamiltonian(n_levels=4, omega=1.0)
eigvals, eigvecs = np.linalg.eigh(H_osc)
print("Truncated oscillator eigenvalues:")
print(np.round(eigvals, 4))

# Embed into 2-qubit system (dim=4 -> 2 qubits)
H_osc_op = Operator(H_osc)  # 4x4 operator compatible with 2 qubits

print("\nMatrix representation used as 2-qubit operator:")
print(H_osc_op.data)
