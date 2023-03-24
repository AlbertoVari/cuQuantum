import cirq
import qsimcirq
import time
n_qubits = 27

qubits = cirq.LineQubit.range(n_qubits)
circuit = cirq.Circuit()
circuit.append(cirq.H(qubits[0]))
circuit.append(cirq.CNOT(qubits[idx], qubits[idx + 1]) \
    for idx in range(n_qubits - 1))
print("Qubits = ",n_qubits,time.ctime())
# Cirqs = cirq.sim.Simulator()
cirq_simulator = cirq.Simulator()
result = cirq_simulator.compute_amplitudes(circuit, [0, 2**n_qubits-1])
print(f'cirq.sim  : {result}',time.ctime())
# qsim(CPU)
options = qsimcirq.QSimOptions(max_fused_gate_size=4, cpu_threads=512)
s = qsimcirq.QSimSimulator(options)
result = s.compute_amplitudes(circuit, [0, 2**n_qubits-1])
print(f'qsim(CPU) : {result}',time.ctime())
# qsim(cuStateVec)
# options = qsimcirq.QSimOptions(use_gpu=True, max_fused_gate_size=4, gpu_mode=1)
options = qsimcirq.QSimOptions(gpu_mode=1)
s = qsimcirq.QSimSimulator(options)
result = s.compute_amplitudes(circuit, [0, 2**n_qubits-1])
print(f'cuStateVec: {result}',time.ctime())