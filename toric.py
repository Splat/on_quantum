from qiskit.quantum_info import SparsePauliOp
import numpy as np

# Define a toy toric-code-like Hamiltonian on 4 qubits
# Here we just use two 4-body stabilizers as an illustration
A_s = SparsePauliOp.from_list([("XXXX", -1.0)])  # star term
B_p = SparsePauliOp.from_list([("ZZZZ", -1.0)])  # plaquette term

H_toric_toy = A_s + B_p
H_mat = H_toric_toy.to_matrix()
eigvals, eigvecs = np.linalg.eigh(H_mat)

print("Toy toric-code-like eigenvalues:")
print(np.round(eigvals, 4))

# Identify ground states (lowest energies)
E0 = eigvals[0]
print("\nLowest-energy eigenvalue:", E0)

# Show structure of one ground state
basis_states = [format(i, '04b') for i in range(16)]
vec0 = eigvecs[:, 0]
print("\nGround state (truncated shown):")
for idx, amp in enumerate(vec0):
    if np.abs(amp) > 0.2:
        print(f"  |{basis_states[idx]}>: amp = {amp:.3f}")
