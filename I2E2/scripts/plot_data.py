import numpy as np
import matplotlib.pyplot as plt
import sys


data = np.loadtxt(sys.argv[1], comments='time', delimiter=',')
fig,axs = plt.subplots(4,1,sharex=True)

start_time = 5000
end_time = 6000

for i in range(4):
    if i < 2:
        color='green'
    else:
        color='black'
    axs[i].plot(data[start_time*10:end_time*10,0], data[start_time*10:end_time*10,i+1],color=color)
plt.xlabel("time (ms)")
plt.show()
