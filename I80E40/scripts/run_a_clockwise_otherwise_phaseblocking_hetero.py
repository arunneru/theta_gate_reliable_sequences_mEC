import sys
import json
import os
import numpy as np

pbs_index = str(sys.argv[1])

dic_params = json.load(open("params_I80E40_clockwise_otherwise_phaseblocking.txt"))
params_list = dic_params[pbs_index]

params_list['numEs'] = 40
params_list['numIs'] = 80

nsetFN = "configure_files/nsets_I80E40_-0.05i2idcmin_0.8i2idcmax_-2.7i2e_8.0extdrive_{p[ampSin]}ampSin_{p[trial]}trial_1initcond_0.015ampNoise_{p[phase]}pibysix_{p[phasedifference]}delpibysix_40.0pulsewidth_het.isf".format(p=params_list)

ssetFN = "configure_files/ssets_I80E40_gei0.02_gie0.2_gii1.0_2.0shiftei_0meanie_randomei.isf".format(p=params_list)

outputFN = "/storage/arun/I80E40/phaseblocking/hetero/output_I80E40_1.5gH_{p[freq]}freq_{p[extdrivefreq]}extdrivefreq_{p[ampSin]}ampSin_{p[i2idcmin]}i2idcmin_{p[i2idcmax]}i2idcmax_{p[i2e]}i2e_{p[gei]}gei_{p[gie]}gie_{p[gii]}gii_{p[shiftei]}shiftei_{p[shiftie]}shiftie_{p[meanie]}meanie_{p[trial]}trial_{p[phase]}pibysix_{p[phasedifference]}delpibysix.txt".format(p=params_list)

params_list['nsetFN'] = nsetFN
params_list['ssetFN'] = ssetFN
params_list['outputFN'] = outputFN

os.system("./bin/insilico_I{p[numIs]}E{p[numEs]}_clockwise_otherwise_phaseblocking_hetero_{p[trial]}trial.out -o {p[outputFN]} -n {p[nsetFN]} -s {p[ssetFN]}".format(p=params_list))
