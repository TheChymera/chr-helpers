__author__="Leonor Garcia Gutierrez"
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import chr_matplotlib

 
 	
#Import data
data_test=np.genfromtxt("data_test.dat",delimiter=' ')


#Create remapped color map, plot any NaN's in black
adapted_cmap = chr_matplotlib.remappedColorMap(plt.get_cmap('seismic'), data=data_test)
masked_array = np.ma.array(data_test, mask=np.isnan(data_test))
adapted_cmap.set_bad(color='black')

#plot
im_difference=plt.imshow(masked_array,cmap=adapted_cmap ,interpolation='bicubic')
plt.colorbar(im_difference,orientation='vertical')

#save plot
plt.savefig("fig_test.png")





