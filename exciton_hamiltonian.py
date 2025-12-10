from qiskit.quantum_info import SparsePauliOp
import numpy as np

def exciton_hamiltonian(eps_e=1.0, eps_h=1.0, g=0.5):
    # Z0 term
    H_z0 = SparsePauliOp.from_list([("ZI", eps_e)])
    # Z1 term
    H_z1 = SparsePauliOp.from_list([("IZ", eps_h)])
    # Coupling term: -g (X0 X1 + Y0 Y1)
    H_xx = SparsePauliOp.from_list([("XX", -g)])
    H_yy = SparsePauliOp.from_list([("YY", -g)])
    return H_z0 + H_z1 + H_xx + H_yy

H_exc = exciton_hamiltonian(eps_e=1.0, eps_h=1.0, g=0.5)
H_mat = H_exc.to_matrix()
eigvals, eigvecs = np.linalg.eigh(H_mat)

print("Exciton-like model eigenvalues:")
print(np.round(eigvals, 4))

basis_states = ["00", "01", "10", "11"]
for k, E in enumerate(eigvals):
    print(f"\nEigenvalue {E:.4f}")
    vec = eigvecs[:, k]
    for idx, amp in enumerate(vec):
        if np.abs(amp) > 0.1:
            print(f"  |{basis_states[idx]}>: amp = {amp:.3f}")
