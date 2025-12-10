# On Quantum

You _can_ talk broadly about “types of quasiparticles”… but actually **modeling each one in Qiskit** is only feasible in simplified toy form. I’ll do this in a way that’s honest but still useful:

1.  **Give you a categorized list of common quasiparticles** with short descriptions.    
2.  **Pick a few representative ones** and show how to build **toy Qiskit models** for them:    
    - Phonons → harmonic-oscillator-like bosonic mode (truncated).        
    - Magnons → spin waves in a small Heisenberg chain.        
    - Anyons → toric-code–style anyons via stabilizers.        
    - Exciton (electron–hole pair) → simple 2-qubit model.        

All code will be standard Python + Qiskit you can run in a notebook (you may need to tweak imports depending on your Qiskit version).

## 1. Main “families” of quasiparticles (high level)

These are _effective_ particles that emerge from many-body systems, usually in condensed matter:

### Bosonic collective modes

- **Phonons**  
    - Lattice vibration quanta (sound/heat in solids).        
    - Come from quantized normal modes of ions in a crystal.        
- **Magnons**  
    - Spin-wave quanta in ordered magnets.        
    - Excitations of a lattice of interacting spins (e.g., Heisenberg model).        
- **Plasmons**  
    - Collective oscillations of the free electron gas in a metal/semiconductor.        
    - Relevant to optical response, surface plasmons, etc.        
- **Polaritons** (e.g., exciton-polaritons)    
    - Hybrid light–matter modes (photon + exciton).        
    - Seen in microcavities, strongly coupled systems.        
- **Photonic quasiparticles in waveguides**  
    - Effective modes in photonic crystals, etc., often treated similarly to phonons/plasmons.        

### Fermionic (or effective fermionic) quasiparticles

- **Electrons with effective mass (Landau quasiparticles)**  
    - In Fermi liquids, interacting electrons behave like free ones but with renormalized parameters.        
- **Holes**  
    - Absence of an electron in a filled band; behave as positive-charge carriers.        
- **Excitons**  
    - Bound electron–hole pair; bosonic (in the low-density limit).        
- **Cooper pairs**  
    - Bound pairs of electrons in superconductors (effective bosons).        

### Dressed particles / combined

- **Polarons**  
    - An electron (or hole) dressed by a cloud of lattice distortion (phonons).        
    - Electron–phonon coupling problem.        
- **Spinons, holons, orbitons**  
    - In certain 1D/strongly correlated systems, spin/charge/orbital degrees of freedom can fractionalize into separate excitations.        

### Topological quasiparticles

- **Anyons** (Abelian and non-Abelian)    
    - Quasiparticles in 2D systems with statistics interpolating between bosons and fermions.        
    - Appear in fractional quantum Hall systems, toric-code models, etc.        
- **Majorana zero modes**  
    - Quasiparticles that are their own antiparticles in certain topological superconductors; candidate building blocks for topological quantum computing.
 
## 2. Qiskit modeling philosophy (important reality check)

Real quasiparticles live in **huge Hilbert spaces** (many sites / continuum modes). On a small simulator / NISQ device, we do:

- **Finite-site spin chains** → magnons, spinons (very small number).    
- **Small fermionic models (Hubbard-like)** → electrons/holes/excitons.    
- **Bosonic truncation** → approximate a harmonic oscillator with a few levels mapped to qubits.    
- **Stabilizer codes** → anyons in toy topological codes (toric/planar code on 4–8 qubits).    

So: we’re not reproducing full condensed-matter physics, we’re building **minimal Hamiltonians and circuits** that capture the _structure_ of the excitations.

