from brian2 import *

Cm = 1*uF/cm**2
gl = 0.3*msiemens/cm**2
El = -54.387*mV
EK = -77*mV
ENa = 50*mV
gNa = 120*msiemens/cm**2
gK = 36*msiemens/cm**2
area = pi * (10*umetre)**2  

eqs = '''
dv/dt = (gNa*m**3*h*(ENa-v) + gK*n**4*(EK-v) + gl*(El-v) + I_stim/area) / Cm : volt
dm/dt = alpham*(1-m)-betam*m : 1
dn/dt = alphan*(1-n)-betan*n : 1
dh/dt = alphah*(1-h)-betah*h : 1
alpham = 0.1/mV*(v+40*mV)/(1-exp(-(v+40*mV)/(10*mV)))/ms : Hz
betam = 4*exp(-(v+65*mV)/(18*mV))/ms : Hz
alphah = 0.07*exp(-(v+65*mV)/(20*mV))/ms : Hz
betah = 1/(1+exp(-(v+35*mV)/(10*mV)))/ms : Hz
alphan = 0.01/mV*(v+55*mV)/(1-exp(-(v+55*mV)/(10*mV)))/ms : Hz
betan = 0.125*exp(-(v+65*mV)/(80*mV))/ms : Hz
I_stim : amp
'''

neuron = NeuronGroup(1, eqs, method='exponential_euler')
neuron.v = El
neuron.m = 'alpham/(alpham+betam)'
neuron.h = 'alphah/(alphah+betah)'
neuron.n = 'alphan/(alphan+betan)'
neuron.I_stim = 0*nA  

M = StateMonitor(neuron, variables=True, record=True)

run(20*ms)
neuron.I_stim = 0.5*nA  
run(100*ms)
neuron.I_stim = 0*nA  
run(100*ms)
print(M.v[0])
