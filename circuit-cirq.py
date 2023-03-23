import cirq
import cupy

from cuquantum import contract, CircuitToEinsum

# create a random cirq.Circuit
circuit = cirq.testing.random_circuit(qubits=4, n_moments=4, op_density=0.9, random_state=1)
# same task can be achieved with qiskit.circuit.random.random_circuit

# construct the CircuitToEinsum converter targeting double precision and cupy operands
converter = CircuitToEinsum(circuit, dtype='complex128', backend='cupy')

# generate the Einstein summation expression and tensor operands for computing the amplitude coefficient of bitstring 0000
expression, operands = converter.amplitude(bitstring='0000')
assert all([isinstance(op, cupy.ndarray) for op in operands])

# contract the network to compute the amplitude
amplitude = contract(expression, *operands)
amplitude_cupy = cupy.einsum(expression, *operands)
assert cupy.allclose(amplitude, amplitude_cupy)
print(circuit,converter,amplitude_cupy)