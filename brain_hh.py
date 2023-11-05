from brian2 import *

Cm = 1*uF/cm**2
gNa = 35*msiemens/cm**2
gK = 9*msiemens/cm**2
gL = 0.1*msiemens/cm**2
ENa = 50*mV
EK = -90*mV
EL = -65*mV

eqs = '''
dv/dt = (gNa*m**3*h*(ENa-v) + gK*n**4*(EK-v) + gL*(EL-v) + I)/Cm : volt
dm/dt = alpha_m*(1-m) - beta_m*m : 1
dn/dt = alpha_n*(1-n) - beta_n*n : 1
dh/dt = alpha_h*(1-h) - beta_h*h : 1
alpha_m = 0.1*(mV**-1)*(25*mV-v+VT)/(exp((25*mV-v+VT)/(10*mV))-1)/ms : Hz
beta_m = 4*exp(-(v-VT)/(18*mV))/ms : Hz
alpha_h = 0.07*exp(-(v-VT)/(20*mV))/ms : Hz
beta_h = 1/(exp((30*mV-v+VT)/(10*mV))+1)/ms : Hz
alpha_n = 0.01*(mV**-1)*(10*mV-v+VT)/(exp((10*mV-v+VT)/(10*mV))-1)/ms : Hz
beta_n = 0.125*exp(-(v-VT)/(80*mV))/ms : Hz
I : amp
'''

neuron = NeuronGroup(1, eqs, method='exponential_euler')
neuron.v = EL
VT = -63*mV 

neuron.m = 'alpha_m / (alpha_m + beta_m)'
neuron.h = 'alpha_h / (alpha_h + beta_h)'
neuron.n = 'alpha_n / (alpha_n + beta_n)'

start_time = 20*ms
duration = 60*ms
neuron.I = TimedArray([0*nA, 0.5*nA, 0*nA], dt=start_time+duration)

M = StateMonitor(neuron, 'v', record=True)

run(100*ms)

plt.figure(figsize=(10, 5))
plt.plot(M.t/ms, M.v[0]/mV)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane potential (mV)')
plt.title('Membrane potential of a Hodgkin-Huxley neuron (Brian2)')
plt.show()
