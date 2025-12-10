from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli

# Prepare ground state from eigen-decomposition
ground_state = Statevector(vec0)

# Define a Z on qubit 0
Z0 = Pauli("ZIII").to_matrix()
excited_state = Statevector(Z0 @ ground_state.data)

# Check expectation values of stabilizers
def expectation(state, op: SparsePauliOp):
    mat = op.to_matrix()
    return np.vdot(state.data, mat @ state.data).real

print("Expectation A_s (ground):", expectation(ground_state, A_s))
print("Expectation B_p (ground):", expectation(ground_state, B_p))
print("Expectation A_s (excited):", expectation(excited_state, A_s))
print("Expectation B_p (excited):", expectation(excited_state, B_p))
