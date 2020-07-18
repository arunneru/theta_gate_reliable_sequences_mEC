import numpy as np

def gen_oneSset(l_pars):
    numEs = 1
    numIs = 1
    numNs = numEs + numIs

    NUMIS = str(numIs)
    NUMES = str(numEs)
    NUMNS = str(numNs)

    gei = l_pars[0]
    gie = l_pars[1]

    
    GEI = str(gei)
    GIE = str(gie)
    
    adjlist = [[0,1,gei],[1,0,gie]]

    outfile = open("configure_files/ssets_I%sE%s_gei%s_gie%s.isf"%(NUMIS,NUMES,GEI,GIE),"w")
    print("configure_files/ssets_I%sE%s_gei%s_gie%s.isf"%(NUMIS,NUMES,GEI,GIE))
    
    strToFile = ""
    for i in range(len(adjlist)):
        syn = i+1
        prN = adjlist[i][0]
        pstN = adjlist[i][1]
        if prN >= numEs:
            g_inh = adjlist[i][2]
            strToFile += "\"synapse %s\"dxdt:1,s:0,gsyn:%f,tau_r:.30,tau_d:9.0,esyn:-80,delay:0.0,pre:%d,post:%d;"%(str(syn),g_inh,prN,pstN)        
        else:
            g_exc = adjlist[i][2]
            strToFile += "\"synapse %s\"dxdt:1,s:0,gsyn:%f,tau_r:0.01,tau_d:3.0,esyn:0,delay:0.0,pre:%d,post:%d;"%(str(syn),g_exc,prN,pstN)

    print(syn)
    outfile.write(strToFile)
    outfile.close()

l_gei = [0.03]
l_gies = [0.0,0.005,0.01,0.015,0.02,0.025,0.03,0.035]

for gei in l_gei:
    for gie in l_gies:
        gen_oneSset([gei,gie])



