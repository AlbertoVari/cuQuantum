
import numpy as np
import pandas as pd

from qiskit import QuantumCircuit, execute, Aer
import  cirq, qsimcirq

#Quantum Circuit
qb = cirq.LineQubit.range(2)
qc = cirq.Circuit()

# Create a quantum circuit with two qubits


# Apply a Hadamard gate to the first qubit
qc.append(cirq.H(qb[0]))

# Apply a CNOT gate to create a Bell state
qc.append(cirq.CNOT(qb[0],qb[1]))

# Measure the qubits and store the results in classical bits
qc.append(cirq.measure(qb[0]))
qc.append(cirq.measure(qb[1]))
# qc.append(cirq.MeasurementGate(qb[0]))
# qc.append(cirq.MeasurementGate(qb[1]))

#print circuit
print("Circuit : ")
print(qc)

# Run the circuit on a simulator
options = qsimcirq.QSimOptions(gpu_mode=1)
simulator = qsimcirq.QSimSimulator(options)

rep = 100
result = simulator.run(qc, repetitions=rep)

result_lines = str(result)

with open('qresult.txt', 'w') as f:
    f.write('\n'.join(result_lines))
    f.close()

print("Results with ",rep," repetitions :" )
print(result)


