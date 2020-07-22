import numpy as np

def gen_oneSset(l_pars):
    numEs = 2
    numIs = 2
    numNs = numEs + numIs

    NUMIS = str(numIs)
    NUMES = str(numEs)
    NUMNS = str(numNs)

    gei = l_pars[0]
    gie = l_pars[1]
    gii = l_pars[2]
    
    GEI = str(gei)
    GIE = str(gie)
    GII = str(gii)
    
    adjlist = [[0,2,gei],[1,3,gei],[2,1,gie],[3,0,gie],[2,3,gii],[3,2,gii]]

    outfile = open("configure_files/ssets_I%sE%s_gei%s_gie%s_%sgii.isf"%(NUMIS,NUMES,GEI,GIE,GII),"w")
    print("configure_files/ssets_I%sE%s_gei%s_gie%s_%sgii.isf"%(NUMIS,NUMES,GEI,GIE,GII))
    
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

l_gei = [0.0,0.03,0.05,0.1]
l_gies = [0.6]
l_gii = [0.2,0.4,0.6,0.8,1.0]

for gei in l_gei:
    for gie in l_gies:
        for gii in l_gii:
            gen_oneSset([gei,gie,gii])



