import sys
import math
import json
import multiprocessing as mp
import numpy as np

def factorial(n):
    if n==1:
        return n
    else:
        ramn = n
        fact = 1
        while ramn >= 2:
            fact *= ramn
            ramn -= 1
        return fact

def nCr(n,r):
    n_fact = np.math.factorial(n)
    r_fact = np.math.factorial(r)
    n_min_r_fact = np.math.factorial(n-r)
    combo = n_fact/(r_fact*n_min_r_fact)
    return combo

def genNsets_once(l_pars):
    freq = l_pars[0]
    ampSin = l_pars[1]
    trial = l_pars[2]
    init_cond = l_pars[3]
    extdrivefreq = l_pars[4]
    phase = l_pars[5]

    numEs = 40
    numIs = 40
    numNs = numIs + numIs
    NUMIS = str(numIs)
    NUMES = str(numEs)
    NUMNS = str(numNs)

    FREQ = str(freq)
    EXTFREQ = str(extdrivefreq)
    AMPSIN = str(ampSin)
    TRIAL = str(trial)
    PHASE = str(phase)
    INITCOND = str(init_cond)

    extwavelen = int((1.0/extdrivefreq)*1000.0*numEs)

    print("extwavelen  ------> ", extwavelen)

    PHASE_ROUND = str(np.round(phase/(np.pi/6.0)))

    outfile = open("configure_files/nsets_I%sE%s_%sfreq_%sampSin_%strial_%sinitcond_%spibysix.isf"%(NUMIS,NUMES,EXTFREQ,AMPSIN,TRIAL,INITCOND,PHASE_ROUND),"w")
    print("configure_files/nsets_I%sE%s_%sfreq_%sampSin_%strial_%sinitcond_%spibysix.isf"%(NUMIS,NUMES,EXTFREQ,AMPSIN,TRIAL,INITCOND,PHASE_ROUND))

    np.random.seed(init_cond)

    asympt = json.load(open("configure_files/asymptode_v_stellate_i2e-3.6.txt"))
    strToFile = ""
    
    for i in range(numEs):
        PMIN = str(np.random.choice(np.arange(-4.0,-3.6,0.1),1)[0]);
        TAURISE = str(np.random.choice(np.arange(20.0,200.0,1.0),1)[0]);
        strToFile += "\"neuron %s\"dxdt:7,v:%s,m:%s,n:%s,h:%s,ms:%s,mhs:%s,mhf:%s,I_DC:0.0,gh:1.5,I_syn:0.0,ampSin:0.0,ampNoise:0.008,freq:0.0,phase:0.0,V_th_Osc:-80,tau_fact:1.0,PulseDuration:10000,PulseStart:1000,PulseEnd:9000,tau_rise:%s,tau_fall:20.0,PulseMax:-2.7,PulseMin:%s,I_PeriodicPulse:0.0,I_OscillatoryDrive:0.0, I_Na_Stellate_HR2005:0.0, I_K_Stellate_HR2005:0.0, I_Leak_Stellate_HR2005:0.0, I_NaP_Stellate_HR2005:0.0, I_Hs_Stellate_HR2005:0.0, I_Hf_Stellate_HR2005:0.0, ;\n\n"%(str(i),str(asympt["v"]),str(asympt["m"]),str(asympt["n"]),str(asympt["h"]),str(asympt["ms"]),str(asympt["mhs"]),str(asympt["mhf"]),TAURISE,PMIN)

    for i in range(numEs,numEs+numIs):
        TAURISE = str(np.random.choice(np.arange(20.0,200.0,1.0),1)[0])
        strToFile += "\"neuron %s \"dxdt:3,v:3.850352,n:0.764751,h:0.283859,I_DC:0.0,ampSin:%s, I_esyn:0.0, I_isyn:0.0, ampNoise:0.015,freq:%s,phase:%s,V_th_Osc:-80,PulseDuration:10000,PulseStart:1000,PulseEnd:9000,tau_rise:%s,tau_fall:20.0,PulseMax:-0.05,PulseMin:-3.1,I_PeriodicPulse:0.0,I_OscillatoryDrive:0.0, I_travelingSwitch:0.0,I_travelingPulse:0.0,pulse:0.0, highDCDuration:%s, highDCMax:0.8, highDCMin:-0.05,  I_Na_InterNeuron_Wang96:0.0, I_K_InterNeuron_Wang96:0.0, I_Leak_InterNeuron_Wang96:0.0, numEs:%s;\n\n"%(str(i),AMPSIN,FREQ,PHASE,TAURISE,str(extwavelen),numEs)
    outfile.write(strToFile)
    outfile.close()

cnt = 0
pibysix = (np.pi/6.0)

l_freqNpulse = []
l_freqNpulse += [[freq,freq] for freq in [8.0]]
l_freqNpulse += [[0.0,freq] for freq in [8.0]]

for freq,extdrivefreq in l_freqNpulse:
    if freq != 0.0:
        ampSin = 0.04
        phase =  4*pibysix
    else:
        ampSin = 0.0
        phase = 0.0
    for trial in [0]:
        for init_cond in [1]:
            genNsets_once([freq,ampSin,trial,init_cond,extdrivefreq,phase])
            cnt += 1
print(cnt)
