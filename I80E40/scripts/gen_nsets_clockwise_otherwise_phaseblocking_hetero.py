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

    gH = l_pars[0]
    i2idcmax = l_pars[1]
    i2e = l_pars[2]
    tau_fact = l_pars[3]
    freq = l_pars[4]
    trial = l_pars[5]
    ampSin = l_pars[6]
    init_cond = l_pars[7]
    ampNoise = l_pars[8]
    extdrivefreq = l_pars[9]
    i2idcmin = l_pars[10]
    phase = l_pars[11]
    phasedifference = l_pars[12]
    pulsewidth = l_pars[13]

    numEs = 40
    numIs = 80
    numNs = numIs + numIs
    NUMIS = str(numIs)
    NUMES = str(numEs)
    NUMNS = str(numNs)

    GH = str(gH)
    EAMPSIN = str(0.0)
    IAMPSIN = str(ampSin)
    FREQ = str(freq)
    PHASE = str(phase)
    TAU_FACT = str(tau_fact)
    TRIAL = str(trial)
    INITCOND = str(init_cond)
    AMPNOISE = str(ampNoise)
    PULSEWIDTH = str(pulsewidth)
    PHASEDIF = str(phasedifference)
  
    I2IDCMIN = str(i2idcmin)
    I2E = str(i2e)
    I2IDCMAX = str(i2idcmax)
    extwavelen = int((1.0/extdrivefreq)*1000.0*numEs)

    print "extwavelen  ------> ", extwavelen
    print
    print
    
    pibysix = np.pi/6.0
    phase_shift = phase * pibysix
    inter_phasedif = phasedifference * pibysix

    outfile = open("configure_files/nsets_I%sE%s_%si2idcmin_%si2idcmax_%si2e_%sextdrive_%sampSin_%strial_%sinitcond_%sampNoise_%spibysix_%sdelpibysix_%spulsewidth_het.isf"%(NUMIS,NUMES,I2IDCMIN,I2IDCMAX,I2E,str(extdrivefreq),IAMPSIN,TRIAL,INITCOND,AMPNOISE,PHASE,PHASEDIF,PULSEWIDTH),"wb")
    print("configure_files/nsets_I%sE%s_%si2idcmin_%si2idcmax_%si2e_%sextdrive_%sampSin_%strial_%sinitcond_%sampNoise_%spibysix_%sdelpibysix_%spulsewidth_het.isf"%(NUMIS,NUMES,I2IDCMIN,I2IDCMAX,I2E,str(extdrivefreq),IAMPSIN,TRIAL,INITCOND,AMPNOISE,PHASE,PHASEDIF,PULSEWIDTH))

    np.random.seed(init_cond)
    #g_vs = n qp.random.random([numEs,8])
    #g_vs[:,0] = np.random.choice(np.arange(-80,-10,0.5))

    asympt = json.load(open("asymptode_v_stellate_i2e-3.6.txt"))
    strToFile = ""
    
    for i in range(numEs):
        PMIN = str(np.random.choice(np.arange(-4.0,-3.6,0.1),1.0)[0])
        TAURISE = str(np.random.choice(np.arange(20.0,200.0,1.0),1)[0])
        IEXT_EXC = I2E
        strToFile += "\"neuron %s\"dxdt:7,v:%s,m:%s,n:%s,h:%s,ms:%s,mhs:%s,mhf:%s,I_DC:0.0,gh:%s,I_syn:0.0,ampSin:%s,ampNoise:0.008,freq:0.0,phase:0.0,V_th_Osc:-80,tau_fact:%s,PulseDuration:10000,PulseStart:1000,PulseEnd:9000,tau_rise:%s,tau_fall:20.0,PulseMax:%s,PulseMin:%s,I_PeriodicPulse:0.0,I_OscillatoryDrive:0.0, I_Na_Stellate_HR2005:0.0, I_K_Stellate_HR2005:0.0, I_Leak_Stellate_HR2005:0.0, I_NaP_Stellate_HR2005:0.0, I_Hs_Stellate_HR2005:0.0, I_Hf_Stellate_HR2005:0.0, ;\n\n"%(str(i),str(asympt["v"]),str(asympt["m"]),str(asympt["n"]),str(asympt["h"]),str(asympt["ms"]),str(asympt["mhs"]),str(asympt["mhf"]),GH,0.0,TAU_FACT,TAURISE,IEXT_EXC,PMIN)#,TFACT)#IEXT_EXC,GH)
    for i in range(numEs,numEs+numIs):
        TAURISE = str(np.random.choice(np.arange(20.0,200.0,1.0),1)[0])

        gk = 11.0 + 0.1*11.0*np.random.randn()
        while gk <= 0.0:
            gk = 11.0 + 0.1*11.0*np.random.randn()

        gl = 0.1 + 0.1*0.1*np.random.randn()
        while gl <= 0.0:
            gl = 0.1 + 0.1*0.1*np.random.randn()
        
        gna = 52 + 0.1*52.0*np.random.randn()
        while gna <= 0.0:
            gna = 52.0 + 0.1*52.0*np.random.randn()
      

        strToFile += "\"neuron %s \"dxdt:3,v:3.850352,n:0.764751,h:0.283859,gl:%s,gk:%s,gna:%s,I_DC:0.0,ampSin:%s, I_esyn:0.0, I_isyn:0.0, ampNoise:%s,freq:%s,phase:%s,phasedifference:%s,V_th_Osc:-80,PulseDuration:10000,PulseStart:1000,PulseEnd:9000,tau_rise:%s,tau_fall:20.0,PulseMax:%s,PulseMin:-3.1,I_PeriodicPulse:0.0,I_OscillatoryDrive:0.0, I_travelingSwitch:0.0,I_travelingPulse:0.0, pulse:0.0, highDCDuration:%s, highDCMax:%s, highDCMin:%s,  I_Na_InterNeuron_Wang96:0.0, I_K_InterNeuron_Wang96:0.0, I_Leak_InterNeuron_Wang96:0.0, numEs:%s, pulsewidth:%s ;\n\n"%(str(i),str(gl),str(gk),str(gna),IAMPSIN,AMPNOISE,FREQ,str(phase_shift),str(inter_phasedif),TAURISE,str(0.0),str(extwavelen),I2IDCMAX,I2IDCMIN,numEs,PULSEWIDTH)
    outfile.write(strToFile)
    outfile.close()

gH = 1.5
tau_fact = 1.0
l_ampSin = [0.06]
l_ampNoise = [0.015]
l_i2e = [-2.7]
l_i2idcmin = [-0.05]
i2e = -2.7
cnt = 0
l_i2idcmax = [0.8]
l_pulsewidth = [20.0]
l_phases = [0.0,2.0,4.0,6.0,8.0,10.0]

l_phasedifference = [3.0,6.0]

l_freqs = [0.0,8.0]


for freq in l_freqs:
    extdrivefreq = 8.0
    if freq != 0.0:
        for ampSin in l_ampSin:
            for trial in range(10):
                for init_cond in [1]:
                    for ampNoise in l_ampNoise:
                        for i2idcmax in l_i2idcmax:
                            for i2idcmin in l_i2idcmin:
                                for phase in l_phases:
                                    for pulsewidth in l_pulsewidth:
                                        for phasedifference in l_phasedifference:
                                            genNsets_once([gH,i2idcmax,i2e,tau_fact,freq,trial,ampSin,init_cond,ampNoise,extdrivefreq,i2idcmin,phase,phasedifference,pulsewidth])
                                            cnt += 1


    else:
        extdrivefreq = 8.0
        ampSin = 0.0
        for trial in range(3):
            for init_cond in [1]:
                for ampNoise in l_ampNoise:
                    for i2idcmax in l_i2idcmax:
                        for i2idcmin in l_i2idcmin:
                            for phase in l_phases:
                                for pulsewidth in l_pulsewidth:
                                    for phasedifference in l_phasedifference:
                                        genNsets_once([gH,i2idcmax,i2e,tau_fact,freq,trial,ampSin,init_cond,ampNoise,extdrivefreq,i2idcmin,phase,phasedifference,pulsewidth])
                                        cnt += 1


print cnt


