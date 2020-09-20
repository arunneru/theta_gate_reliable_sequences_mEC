import numpy as np
import matplotlib.pyplot as plt


fig,axs = plt.subplots((nNeurons,1))

freq = 0.0

for neuron in range(40):
    for trial in range(10):
        spiketime_file = open("spike_times/spike_times_{}freq_{}trial_{}neuron.txt".format(freq,trial,neuron))

        spiketime_str_list = spiketime_file.readlines()
        spiketime_strCompact_list = spiketime_str_list[0].strip()
        spiketime_float_list =  spiketime_strCompact_list.split()
        for iter_str in range(len(spiketime_float_list)):
            spiketime_float_list[iter_str] = float(spiketime_float_list[iter_str])

        axs[neuron].eventplot(spikeime_float_list,lineoffsets=[trial*1.2],linelengths=[1],color='k')
        axs[neuron].axhline(y=-0.65,color='k',linestyle='--')
    axs[neuron].set_axis_off()
    
fig.set_size_inches(8,8)
plt.savefig('raster_without_theta.png',format='png',dpi=300)
plt.close()

fig,axs = plt.subplots((nNeurons,1))

freq = 0.0

for neuron in range(40):
    for trial in range(10):
        spiketime_file = open("spike_times/spike_times_{}freq_{}trial_{}neuron.txt".format(freq,trial,neuron))

        spiketime_str_list = spiketime_file.readlines()
        spiketime_strCompact_list = spiketime_str_list[0].strip()
        spiketime_float_list =  spiketime_strCompact_list.split()
        for iter_str in range(len(spiketime_float_list)):
            spiketime_float_list[iter_str] = float(spiketime_float_list[iter_str])

        axs[neuron].eventplot(spikeime_float_list,lineoffsets=[trial*1.2],linelengths=[1],color='k')
        axs[neuron].axhline(y=-0.65,color='k',linestyle='--')
    axs[neuron].set_axis_off()
    
fig.set_size_inches(8,8)
plt.savefig('raster_with_theta.png',format='png',dpi=300)
plt.close()

