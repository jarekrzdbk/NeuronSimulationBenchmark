from neuron import h, gui
import matplotlib.pyplot as plt

soma = h.Section(name='soma')

soma.insert('hh')

soma.L = 20  
soma.diam = 20  

v = h.Vector().record(soma(0.5)._ref_v)  
t = h.Vector().record(h._ref_t)  

stim = h.IClamp(soma(0.5))
stim.delay = 20  
stim.dur = 60    
stim.amp = 0.5  

h.finitialize(-65)  
h.continuerun(100) 
for t_1, v_1 in zip(t, v):
    print('Time: {:.3f} ms, Membrane potential: {:.3f} mV'.format(t_1, v_1))
#plt.figure(figsize=(10, 5))
#plt.plot(t, v)
#plt.xlabel('Time (ms)')
#plt.ylabel('Membrane potential (mV)')
#plt.title('Membrane potential of a Hodgkin-Huxley neuron (NEURON)')
#plt.show()
