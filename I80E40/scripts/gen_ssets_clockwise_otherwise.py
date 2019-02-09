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

def circular_shift(my_l,by):
    if by == 0:
        return my_l
    else:
        return my_l[by:] + my_l[:by]

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
    
    numEs = 40
    numIs = 40
    numNs = numEs+numIs
    print("shiftei ", shiftei)
    gei =  0.02
    gie = 0.2
    gii = 1.0
    gPsize = 1

    NUMES = str(numEs)
    NUMIS = str(2*numIs)
    GEI = str(gei)
    GIE = str(gie)
    GII = str(gii)
    SHIFTEI = str(shiftei)
    MEANIE = str(meanie)
    
    #print(SHIFTEI)
    outfile_adj = open("configure_files/adj_I%sE%s_%sshiftei_%smeaniereverse.isf"%(NUMIS,NUMES,SHIFTEI,MEANIE),"w")
    outfile = open("configure_files/ssets_I%sE%s_gei%s_gie%s_gii%s_%sshiftei_%smeanie_randomei.isf"%(NUMIS,NUMES,GEI,GIE,GII,SHIFTEI,MEANIE),"w")
    print("configure_files/ssets_I%sE%s_gei%s_gie%s_gii%s_%sshiftei_%smeanie_randomei.isf"%(NUMIS,NUMES,GEI,GIE,GII,SHIFTEI,MEANIE))

    adjlist = []
    for chsni in range(numIs):
        pos_ws1 = (gie/0.5)*gen_iekernel(chsni,0.0,meanie,.80,numEs)
        count = 0
        for e in range(numEs):
            weight = pos_ws1[count]
            if weight > (gie/0.6)*0.005:
                adjlist.append([chsni+numEs,e,weight])
            count += 1
        if (chsni == 20):# or (chsni == 10) or (chsni == 39):
            plt.plot(range(numEs),pos_ws1,'ro-')

    i_cnt = numIs + numEs
    l_shifted_numIs = circular_shift(list(range(numIs)),20)
    for chsni in l_shifted_numIs:
        pos_ws1 = (gie/0.5)*gen_iekernel(chsni,0.0,meanie,.80,numEs)
        count = 0
        for e in range(numEs):
            weight = pos_ws1[count]
            if weight > (gie/0.6)*0.005:
                adjlist.append([i_cnt,e,weight])
            count += 1
        if (chsni == 60):
            plt.plot(range(numEs),pos_ws1,'ro-')
        i_cnt += 1

    l_eiweights = np.loadtxt("eiweights_E2I.dat")
    l_eiweights = l_eiweights.tolist()
    l_eiweights = 2*l_eiweights
    print(l_eiweights)
    for chsne in range(numEs):
        pos_is = np.random.choice(np.arange(40,120),12)
        count = 0
        for i in pos_is:
            weight = l_eiweights[count]
            adjlist.append([chsne,i,(gei/0.08)*weight])
            count += 1
        if (chsne == 20):
            plt.plot(pos_is,l_eiweights,'go-')

    for i in range(2*numEs):
        for j in range(i+1,2*numEs):
            adjlist.append([i+numEs,j+numEs,gii])
            adjlist.append([j+numEs,i+numEs,gii])
    np.random.seed(2)
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
    for adj in adjlist:
        
        outfile_adj.write(str(adj[0]))
        outfile_adj.write(" ")
        outfile_adj.write(str(adj[1]))
        outfile_adj.write(" ")
        outfile_adj.write(str(adj[2]))
        outfile_adj.write("\n")
        
    outfile.close()
    outfile_adj.close()

    plt.show()

pool = mp.Pool(20)
l_meanies = [0]#[i for i in range(1,3)]
l_shifteis = [2.0]#np.arange(2.0,12.0,2.0)#2.0

for meanie in l_meanies:
    for shiftei in l_shifteis:
        l_pars = [shiftei,meanie]
        gen_oneSset(l_pars)
