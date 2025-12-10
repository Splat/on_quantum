# On Quantum

You _can_ talk broadly about “types of quasiparticles”… but actually **modeling each one in Qiskit** is only feasible in simplified toy form. I’ll do this in a way that’s honest but still useful:

1.  **Give you a categorized list of common quasiparticles** with short descriptions.    
2.  **Pick a few representative ones** and show how to build **toy Qiskit models** for them:    
    - Phonons → harmonic-oscillator-like bosonic mode (truncated).        
    - Magnons → spin waves in a small Heisenberg chain.        
    - Anyons → toric-code–style anyons via stabilizers.        
    - Exciton (electron–hole pair) → simple 2-qubit model.        

All code will be standard Python + Qiskit you can run in a notebook (you may need to tweak imports depending on your Qiskit version).
