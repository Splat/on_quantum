from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
import numpy as np

def heisenberg_chain_hamiltonian(num_qubits=3, J=-1.0):
    """
    Build H = J * sum_i (X_i X_{i+1} + Y_i Y_{i+1} + Z_i Z_{i+1})
    with periodic boundary conditions.
    """
    paulis = []
    coeffs = []

    for i in range(num_qubits):
        j = (i + 1) % num_qubits
        
        # Helper: build a Pauli string for operator acting on i, j
        def two_site(term_i, term_j):
            # term_i, term_j are 'I', 'X', 'Y', or 'Z'
            # Build full string like "IXI" etc.
            s = ['I'] * num_qubits
            s[i] = term_i
            s[j] = term_j
            return "".join(s)
        
        for term in [('X', 'X'), ('Y', 'Y'), ('Z', 'Z')]:
            paulis.append(two_site(term[0], term[1]))
            coeffs.append(J)

    return SparsePauliOp(paulis, coeffs)

# Build and diagonalize
num_qubits = 3
H = heisenberg_chain_hamiltonian(num_qubits=num_qubits, J=-1.0)

# Convert to dense matrix for small system
H_mat = H.to_matrix()
eigvals, eigvecs = np.linalg.eigh(H_mat)

print("Eigenvalues:")
print(np.round(eigvals, 4))

# Show eigenvectors in computational basis
basis_states = [format(i, '0{}b'.format(num_qubits)) for i in range(2**num_qubits)]

print("\nOne-magnon-like eigenstates (weight in single-flip subspace):")
for k, E in enumerate(eigvals):
    vec = eigvecs[:, k]
    # Compute weight in subspace with exactly one '1'
    weight_one_flip = 0.0
    for idx, amp in enumerate(vec):
        s = basis_states[idx]
        if s.count('1') == 1:
            weight_one_flip += np.abs(amp)**2
    if weight_one_flip > 0.9:  # mostly one-magnon
        print(f"Eigenvalue {E:.4f}, weight in one-flip subspace {weight_one_flip:.3f}")
        for idx, amp in enumerate(vec):
            if np.abs(amp) > 0.1:
                print(f"  |{basis_states[idx]}>: amp = {amp:.3f}")
        print()
