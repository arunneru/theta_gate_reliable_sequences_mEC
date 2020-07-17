import os
import numpy as np
import multiprocessing as mp
import time

def run_once(d_params):
    nsetFN = "configure_files/nsets_I2E2_switching_{p[i2i]}i2i.isf".format(p=d_params)
    outputFN = "dir_output/output_gei{p[gei]}_gie{p[gie]}_{p[gii]}gii_{p[i2i]}i2i.dat".format(p=d_params)
    d_params['outputFN'] = outputFN
    d_params['nsetFN'] = nsetFN
        
    os.system("./bins/insilico_I2E2_switching_autonomous_0trial.out -o {p[outputFN]} -n {p[nsetFN]} ".format(p=d_params))

st_t = time.time()
pool = mp.Pool()

cnt = 0
l_i2is = [0.1,0.2,0.3]

l_dparams = []

for i2i in l_i2is:
    for gei in l_geis:
        for gie in l_gies:
            for gii in l_giis:
                l_dparams.append({'numEs':str(2),'numIs':str(2),'i2i':str(i2i),'gie':str(gie),'gei':str(gei),'gii':str(gii)})
                cnt += 1

print(cnt)
pool.map(run_once,l_dparams)
end_t = time.time()

print("It took ", (end_t - st_t )/60.0 ," minutes to run the entire set of simulations!!")
