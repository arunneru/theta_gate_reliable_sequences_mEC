import sys
import math
import json
import multiprocessing as mp
import numpy as np

def genNsets_once(l_pars):
    i2i = l_pars[0]
    init_cond = l_pars[1]
    freq = l_pars[2]
    ampSin = l_pars[3]
    
    
    numEs = 1
    numIs = 1
    numNs = numIs + numIs
    NUMIS = str(numIs)
    NUMES = str(numEs)
    NUMNS = str(numNs)
    
    INITCOND = str(init_cond)
    
    I2I = str(i2i)
    
    outfile = open("configure_files/nsets_Network_%si2i.isf"%str(i2i),"w")
    print("configure_files/nsets_Network_%si2i.isf"%str(i2i))

    np.random.seed(init_cond)
    #g_vs = n qp.random.random([numEs,8])
    #g_vs[:,0] = np.random.choice(np.arange(-80,-10,0.5))

    asympt = json.load(open("configure_files/asymptode_v_stellate_i2e-3.6.txt"))
    strToFile = ""
    
    for i in range(numEs):
        PMIN = -3.6
        TAURISE = str(np.random.choice(np.arange(100.0,300.0,1.0),1)[0])
        strToFile += "\"neuron %s\"dxdt:7,v:%s,m:%s,n:%s,h:%s,ms:%s,mhs:%s,mhf:%s,gh:1.5,I_syn:0.0,ampSin:0.0,ampNoise:0.008,freq:0.0,phase:0.0,V_th_Osc:-80,tau_fact:1.0,PulseDuration:10000,PulseStart:500,PulseEnd:9500,tau_rise:%s,tau_fall:20.0,PulseMax:-2.7,PulseMin:%s,I_PeriodicPulse:0.0,I_OscillatoryDrive:0.0, I_Na_Stellate_HR2005:0.0, I_K_Stellate_HR2005:0.0, I_Leak_Stellate_HR2005:0.0, I_NaP_Stellate_HR2005:0.0, I_Hs_Stellate_HR2005:0.0, I_Hf_Stellate_HR2005:0.0, ;\n\n"%(str(i),str(asympt["v"]),str(asympt["m"]),str(asympt["n"]),str(asympt["h"]),str(asympt["ms"]),str(asympt["mhs"]),str(asympt["mhf"]),TAURISE,PMIN)
    for i in range(numEs,numEs+numIs):
        IEXT_INH = I2I
        if (i == 2) :
            tau_rise = 300
            IEXT_INH = str(i2i)
        else:
            tau_rise = 20
            IEXT_INH = str(i2i)
        strToFile += "\"neuron %s \"dxdt:3,v:3.850352,n:0.764751,h:0.283859,I_DC:0.0,ampSin:%s,ampNoise:0.015,freq:%s,phase:0.0,V_th_Osc:-80,PulseDuration:10000,PulseStart:500,PulseEnd:9500,tau_rise:20.0,tau_fall:20.0,PulseMax:%s,PulseMin:-0.05,I_PeriodicPulse:0.0,I_syn:0.0,I_OscillatoryDrive:0.0, I_Na_InterNeuron_Wang96:0.0, I_K_InterNeuron_Wang96:0.0, I_Leak_InterNeuron_Wang96:0.0 ;\n\n"%(str(i),str(ampSin), str(freq), IEXT_INH)
    outfile.write(strToFile)
    outfile.close()

l_i2is = [0.1,0.2,0.3,0.4,0.5]

cnt = 0

l_phases = [0]
freq = 7.0
ampSin = 0.05

for init_cond in [1]:
    for i2i in l_i2is:
        genNsets_once([i2i,init_cond,freq,ampSin])
        cnt += 1

print(cnt)
