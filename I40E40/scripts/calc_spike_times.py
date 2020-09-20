import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

def calc_spike_times(d_params):

    nNeurons = d_params['nNeurons']
    
    outputFN = "dir_output/output_I40E40_{p[extdrivefreq]}freq_{p[ampSin]}ampSin_0.03gei_0.3gie_1.0gii_randomei_{p[trial]}trial_1initcond_{p[phase]}pibysix_noreplace.txt".format(p=d_params)
    for neuron in range(nNeurons):
        d_params['neuron'] = neuron
        outfile = open("spike_times/spike_times_{p[freq]}freq_{p[trial]}trial_{p[neuron]}neuron.txt".format(p=d_params),"w")     
        v = np.loadtxt(FN,comments='time',delimiter=',')
        t = v[::10,0]
        v = v[::10,neuron+1]

        preT = v[:-1]-v[1:]
        postT = v[1:]-v[:-1]

        when_spiked = []

        #for j in range(numEs):
        for i in range(len(v[1:-1])):
            if (preT[i] < 0) and (postT[i+1] < 0) and (v[i+1]>-40) and (t[i+1] >= 1500.0 ) and (t[i+1] < 9000.0):
                outfile.write(str(t[i+1]))
                outfile.write(" ")
        outfile.write("\n")
        outfile.close()


pool = mp.Pool() 
pibysix = (np.pi/6.0)

l_freqNpulse = []
l_freqNpulse += [[freq,freq] for freq in [8.0]]
l_freqNpulse += [[0.0,freq] for freq in [8.0]]

l_dparams = []


for freq,extdrivefreq in l_freqNpulse:
    if freq != 0.0:
        ampSin = 0.04
        phase =  4.0
    else:
        ampSin = 0.0
        phase = 0.0
    for trial in range(10):
        for init_cond in [1]:
            l_dparams.append({'nNeurons':str(40),'freq':str(freq),'ampSin':str(ampSin),'trial':str(trial),'init_cond':str(init_cond),'extdrivefreq':str(extdrivefreq),'phase':str(phase)})


pool.map(calc_spike_times,l_params)
end_t = time.time()
print("It took ", (end_t - st_t )/60.0 ," minutes to run the entire set of simulations!!")



