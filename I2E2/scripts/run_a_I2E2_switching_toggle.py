import os
import numpy as np
import multiprocessing as mp
import time

def run_once(d_params):
    nsetFN = "configure_files/nsets_I2E2_switching_{p[i2i]}i2i_{p[dcmax]}dcmax_{p[shift]}shift_40dcwidth.isf".format(p=d_params)
    ssetFN = "configure_files/ssets_I2E2_gei{p[gei]}_gie{p[gie]}_{p[gii]}gii.isf".format(p=d_params)
    outputFN = "dir_output/output_gei{p[gei]}_gie{p[gie]}_{p[gii]}gii_{p[i2i]}i2i_{p[shift]}shift_{p[dcmax]}dcmax.dat".format(p=d_params)
    d_params['outputFN'] = outputFN
    d_params['nsetFN'] = nsetFN
    d_params['ssetFN'] = ssetFN
    os.system("./bins/insilico_I2E2_switching_toggle_0trial.out -o {p[outputFN]} -n {p[nsetFN]} -s {p[ssetFN]}".format(p=d_params))

st_t = time.time()
pool = mp.Pool()

cnt = 0
l_i2is = [0.5,1.0]
l_geis = [0.03]
l_gies = [0.6]
l_giis = [1.0]
l_dcmax = [3.0,4.0,5.0]
l_dcwidth = [40]
l_shift = [0,40]

l_dparams = []

for i2i in l_i2is:
    for gei in l_geis:
        for gie in l_gies:
            for gii in l_giis:
                for dcmax in l_dcmax:
                    for dcwidth in l_dcwidth:
                        for shift in l_shift:
                            l_dparams.append({'numEs':str(2),'numIs':str(2),'i2i':str(i2i),'gie':str(gie),'gei':str(gei),'gii':str(gii),'dcmax':str(dcmax),'dcwidth':str(dcwidth),'shift':str(shift)})
                            cnt += 1
print(cnt)
pool.map(run_once,l_dparams)
end_t = time.time()

print("It took ", (end_t - st_t )/60.0 ," minutes to run the entire set of simulations!!")
