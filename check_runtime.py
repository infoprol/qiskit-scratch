from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler


eg_cir = QuantumCircuit(2)
eg_cir.measure_all()

svc = QiskitRuntimeService()
backend = svc.least_busy(operational=True, simulator=False)

sampler = Sampler(backend)
job = sampler.run([eg_cir])
print(f'job id: {job.job_id()}')

ans = job.result()
print(ans)


