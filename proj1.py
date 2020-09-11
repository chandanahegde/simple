import pandas as pd
import numpy as np
data = pd.read_csv('/home/chandana/CUK/mu-0.txt',sep='\t')
data = np.array(data)
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
x = data[:,4]
y = data[:,5]
z = data[:,6]
plt.plot(y, x,'r--',label='posx')
plt.plot(y, z, 'b--',label='posz')
plt.xlabel('posy')
plt.ylabel('posx, posz')
plt.legend()
plt.show()



