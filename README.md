# Neuron Simulation Project

## Overview
This project compares performance of selected neuron simulators. We compare NEURON, Nest, and Brian2, using PyNN for neuron simulation.

## Results
### Comparison of Neuron Simulators running with PyNN

| Simulator | Time    | Memory Usage |
|-----------|---------|--------------|
| NEURON    | 0:00.73 | 104,728 KB   |
| Brian2    | 0:03.29 | 164,108 KB   |

### Comparison of Neuron Simulators Natively Using Original API of Each Respective Simulator

| Simulator | Time    | Memory Usage |
|-----------|---------|--------------|
| NEURON    | 0:00.76 | 66,156 KB    |
| Brian2    | 0:06.48 | 246,076 KB   |

## How to Run
1. Clone the repository.
2. Install dependencies using Conda: `conda env create -f environment.yml`
3. Activate the Conda environment: `conda activate [env_name]`
4. To run the benchmarks:
   - `./benchmark.sh` for the benchmark using pyNN.
   - `./original_benchmark.sh` for the benchmark without pyNN.

