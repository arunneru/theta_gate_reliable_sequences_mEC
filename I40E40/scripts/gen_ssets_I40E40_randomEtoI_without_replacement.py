import matplotlib.pyplot as plt
import numpy as np
import multiprocessing as mp

"""
G=nx.cubical_graph()
#G1 = nx.DiGraph()
pos=nx.spring_layout(G) # positions for all nodes

# pos = {ind:array([x,y])}

# nodes
nx.draw_networkx_nodes(G,pos,
                       nodelist=[0,1,2,3],
                       node_color='r',
                       node_size=500,
                   alpha=0.8)
nx.draw_networkx_nodes(G,pos,
                       nodelist=[4,5,6,7],
                       node_color='b',
                       node_size=500,
                   alpha=0.8)

# edges
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
nx.draw_networkx_edges(G,pos,
                       edgelist=[(0,1),(1,2),(2,3),(3,0)],
                       width=8,alpha=0.5,edge_color='r')
nx.draw_networkx_edges(G,pos,
                       edgelist=[(4,5),(5,6),(6,7),(7,4)],
                       width=8,alpha=0.5,edge_color='b')


# some math labels
labels={}
labels[0]=r'$a$'
labels[1]=r'$b$'
labels[2]=r'$c$'
labels[3]=r'$d$'
labels[4]=r'$\alpha$'
labels[5]=r'$\beta$'
labels[6]=r'$\gamma$'
labels[7]=r'$\delta$'
nx.draw_networkx_labels(G,pos,labels,font_size=16)

plt.axis('off')
plt.savefig("labels_and_colors.png") # save as png
plt.show() # display
"""

def calc_dist(i,j,numEs):
    return np.min((np.abs(i-j), np.abs(numEs - np.abs(i-j))))

def gen_iekernel(neu_ind,rad,mean,spread,numEs):
    l_numEs = range(numEs)
    l_ws = []

    for i in range(len(l_numEs)):
        dist = calc_dist(neu_ind,i,numEs)
        ws = (1.0/np.sqrt((2.0*np.pi*(spread**2))))*np.exp(-(dist - rad)**2/(2*spread**2))
        l_ws.append(ws)
    if mean:
        l_ws = l_ws[mean:] + l_ws[:mean]
    return np.array(l_ws)

def gen_eikernel(neu_ind,rad,mean,spread,numEs):
    l_numEs = range(numEs)
    l_ws = []

    for i in range(len(l_numEs)):
        dist = calc_dist(neu_ind,i,numEs)
        ws = (1.0/np.sqrt((2.0*np.pi*(spread**2))))*np.exp(-(dist - rad)**2/(2*spread**2))
        l_ws.append(ws)
    if mean:
        l_ws = l_ws[mean:] + l_ws[:mean]
    return np.array(l_ws)

def gen_oneSset(l_pars):
    shiftei = l_pars[0]
    meanie = l_pars[1]
    gie = l_pars[2]
    gei = l_pars[3]
    con_cnt = l_pars[4]

    numEs = 40
    numIs = 40
    numNs = numEs+numIs
    print("shiftei ", shiftei)
    gii = 1.0
    gPsize = 1

    NUMES = str(numEs)
    NUMIS = str(numIs)
    GEI = str(gei)
    GIE = str(gie)
    GII = str(gii)
    SHIFTEI = str(shiftei)
    MEANIE = str(meanie)
    
    #print(SHIFTEI)
    
    np.random.seed(con_cnt)

    outfile_adj = open("configure_files/adj_I%sE%s_randomei_%smeaniereverse_%sseed_withoutreplacement.isf"%(NUMIS,NUMES,MEANIE,str(con_cnt)),"w")
    outfile = open("configure_files/ssets_I%sE%s_gei%s_gie%s_gii%s_randomei_%smeaniereverse_%sseed_noreplace.isf"%(NUMIS,NUMES,GEI,GIE,GII,MEANIE,str(con_cnt)),"w")
    print("configure_files/ssets_I%sE%s_gei%s_gie%s_gii%s_randomei_%smeaniereverse_%sseed_noreplace.isf"%(NUMIS,NUMES,GEI,GIE,GII,MEANIE,str(con_cnt)))

    adjlist = []
    sp_count = 0
    for chsni in range(numIs):
        pos_ws1 = (gie/0.5)*gen_iekernel(chsni,0.0,meanie,.80,numEs)
        count = 0
        for e in range(numEs):
            weight = pos_ws1[count]
            
            if weight > 0.005:
                adjlist.append([chsni+numEs,e,weight])
            count += 1
        if (chsni == 20):# or (chsni == 10) or (chsni == 39):
            plt.plot(range(numEs),pos_ws1,'ro-')
    l_eiweights = np.loadtxt("configure_files/eiweights_E2I.dat")
    for chsne in range(numEs):
        pos_is = []
        while len(pos_is) < 6:
            rand_targ = np.random.choice(np.arange(40,80)) 
            while rand_targ in pos_is:
                rand_targ = np.random.choice(np.arange(40,80))
            pos_is.append(rand_targ)
        count = 0
        for i in pos_is:
            weight = l_eiweights[count]
            adjlist.append([chsne,i,(gei/0.08)*weight])
            count += 1
        if (chsne == 20):
            plt.plot(pos_is,l_eiweights,'go-')

    for i in range(numEs):
        for j in range(i+1,numEs):
            adjlist.append([i+numEs,j+numEs,gii])
            adjlist.append([j+numEs,i+numEs,gii])

    strToFile = ""
    
    for i in range(len(adjlist)):
        syn = i+1
        prN = adjlist[i][0]
        pstN = adjlist[i][1]
        if prN >= numEs:
            if pstN < numEs:
                g_inh = adjlist[i][2]
                strToFile += "\"synapse %s\"dxdt:1,s:0,gsyn:%f,tau_r:.30,tau_d:9.0,esyn:-80,delay:0.0,pre:%d,post:%d;"%(str(syn),g_inh,prN,pstN)
            else:
                g_inh = adjlist[i][2]
                strToFile += "\"synapse %s\"dxdt:1,s:0,gsyn:%f,tau_r:.30,tau_d:9.0,esyn:-80,delay:0.0,pre:%d,post:%d;"%(str(syn),g_inh,prN,pstN)
        else:
            g_exc = adjlist[i][2]
            strToFile += "\"synapse %s\"dxdt:1,s:0,gsyn:%f,tau_r:0.3,tau_d:6.0,esyn:0,delay:0.0,pre:%d,post:%d;"%(str(syn),g_exc,prN,pstN)
    print(syn)
    outfile.write(strToFile)
    for adj in adjlist:
        if (adj[0] >= numEs) and (adj[1] < numEs):
            print(adj)
        outfile_adj.write(str(adj[0]))
        outfile_adj.write(" ")
        outfile_adj.write(str(adj[1]))
        outfile_adj.write(" ")
        outfile_adj.write(str(adj[2]))
        outfile_adj.write("\n")
    outfile.close()
    outfile_adj.close()
    print(sp_count)

pool = mp.Pool(1)
l_meanies = [0]
l_shifteis = [2.0]
l_geis = [0.03]
l_gies = [0.3]

con_cnt = 0
for meanie in l_meanies:
    for shiftei in l_shifteis:
        for gei in l_geis:
            for gie in l_gies:
                l_pars = [shiftei,meanie,gie,gei,con_cnt]
                gen_oneSset(l_pars)
