import os
import numpy as np
import multiprocessing as mp
import time

def run_once(d_params):
    nsetFN = "configure_files/nsets_I40E40_{p[extdrivefreq]}freq_{p[ampSin]}ampSin_{p[trial]}trial_1initcond_{p[phase]}pibysix.isf".format(p=d_params)
    ssetFN = "configure_files/ssets_I40E40_gei0.03_gie0.3_gii1.0_randomei_0meaniereverse_0seed_noreplace.isf"
    outputFN = "dir_output/output_I40E40_{p[extdrivefreq]}freq_{p[ampSin]}ampSin_0.03gei_0.3gie_1.0gii_randomei_{p[trial]}trial_1initcond_{p[phase]}pibysix_noreplace.txt".format(p=d_params)
    d_params['outputFN'] = outputFN
    d_params['nsetFN'] = nsetFN
    d_params['ssetFN'] = ssetFN
    print(outputFN)
    os.system("./bins/insilico_I40E40_varPulse_{p[trial]}trial.out -o {p[outputFN]} -n {p[nsetFN]} -s {p[ssetFN]}".format(p=d_params))

st_t = time.time()
pool = mp.Pool(6)


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
            l_dparams.append({'freq':str(freq),'ampSin':str(ampSin),'trial':str(trial),'init_cond':str(init_cond),'extdrivefreq':str(extdrivefreq),'phase':str(phase)})

pool.map(run_once,l_dparams)
end_t = time.time()

print("It took ", (end_t - st_t )/60.0 ," minutes to run the entire set of simulations!!")
