"""
A simple example of a Hodgkin-Huxley neuron model with PyNN
"""

from pyNN.utility import get_simulator, init_logging, normalized_filename

# === Get the simulator from the command line ================================

sim, options = get_simulator(
    ("--plot-figure", "Plot the simulation results to a file.", {"action": "store_true"}),
    ("--debug", "Print debugging information", {"action": "store_true"})
)

if options.debug:
    init_logging(None, debug=True)

sim.setup(timestep=0.01, min_delay=1.0)

# === Create a single Hodgkin-Huxley neuron ==================================

hh_neuron = sim.Population(1, sim.HH_cond_exp())

# === Inject a current pulse into the neuron =================================

current_source = sim.DCSource(amplitude=0.5, start=20.0, stop=80.0)
hh_neuron.inject(current_source)

# === Record the membrane potential ==========================================

hh_neuron.record('v')

# === Run the simulation =====================================================

sim.run(100.0)  # Run for 100 ms

# === Retrieve and save the recorded data ====================================

data = hh_neuron.get_data().segments[0].analogsignals[0]
times = data.times
voltages = data
print(voltages)

# === Optionally plot a figure ===============================================

if options.plot_figure:
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(times, voltages)
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane potential (mV)')
    plt.title('Membrane potential of a Hodgkin-Huxley neuron')
    plt.show()

# === Clean up and quit ======================================================

sim.end()
