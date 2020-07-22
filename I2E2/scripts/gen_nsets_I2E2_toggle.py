import sys
import math
import json
import multiprocessing as mp
import numpy as np

def genNsets_once(l_pars):
    i2i = l_pars[0]
    init_cond = l_pars[1]
    dcmax = l_pars[2]
    dcwidth = l_pars[3]
    dcduration = 1000.0/8.0
    shift = l_pars[4]
    
    numEs = 2
    numIs = 2
    numNs = numIs + numIs
    NUMIS = str(numIs)
    NUMES = str(numEs)
    NUMNS = str(numNs)
    
    INITCOND = str(init_cond)
    
    I2I = str(i2i)
    
    outfile = open("configure_files/nsets_I2E2_switching_%si2i_%sdcmax_%sshift_%sdcwidth.isf"%(str(i2i),str(dcmax),str(shift),str(dcwidth)),"w")
    print("configure_files/nsets_I2E2_switching_%si2i_%sdcmax_%sshift_%sdcwidth.isf"%(str(i2i),str(dcmax),str(shift),str(dcwidth)))

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
        strToFile += "\"neuron %s \"dxdt:3,v:3.850352,n:0.764751,h:0.283859,I_DC:0.0,ampSin:0.0,ampNoise:0.015,freq:0.0,phase:0.0,V_th_Osc:-80,PulseDuration:10000,PulseStart:500,PulseEnd:9500,tau_rise:20.0,tau_fall:20.0,PulseMax:%s,PulseMin:-0.05,highDCMin:0.0,highDCMax:%s,pulsewidth:%s,highDCDuration:%s,shiftInMsec:%s,I_PeriodicPulse:0.0,I_syn:0.0,I_OscillatoryDrive:0.0, I_Na_InterNeuron_Wang96:0.0, I_K_InterNeuron_Wang96:0.0, I_Leak_InterNeuron_Wang96:0.0 ;\n\n"%(str(i),IEXT_INH,str(dcmax),str(dcwidth),str(dcduration),str(shift))
        
    outfile.write(strToFile)
    outfile.close()

l_i2is = [0.5,1.0]
l_dcmax = [3.0,4.0,5.0]
l_dcwidth = [40]
l_shift = [0,40]

cnt = 0

for i2i in l_i2is:
    for init_cond in [1]:
        for dcmax in l_dcmax:
            for dcwidth in l_dcwidth:
                for shift in l_shift:
                    genNsets_once([i2i,init_cond,dcmax,dcwidth,shift])
                    cnt += 1
print(cnt)
