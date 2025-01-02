from qiskit_ibm_runtime import QiskitRuntimeService

import os

toke = None
try: toke = os.environ['IBM_Q_API_KEY']
except KeyError:
    print('please save your ibm quantum platform api key to IBM_Q_API_KEY and try again!')
    exit()

QiskitRuntimeService.save_account(
        token=toke,
        channel='ibm_quantum')


print('creds should be saved at ~/.qiskit/qiskit-ibm.json')
