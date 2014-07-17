import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import imp
col = imp.load_source('remappedColorMap', './../chr_matplotlib.py')

#Generate test data, with offset
test_data = np.random.rand(40,40)-0.3

#Create remapped color map
original_cmap = plt.get_cmap('seismic')
remapped_cmap = col.remappedColorMap(original_cmap, data=test_data)

#Plots:
#(1) Original Cmap
plt.subplot(2, 1, 1)
test_plot2=plt.imshow(test_data,cmap=plt.get_cmap('seismic') ,interpolation='bicubic')
plt.title("Original Cmap")
divider = make_axes_locatable(plt.gca())
plt.colorbar(test_plot2,orientation='vertical', cax=divider.append_axes("right", size="5%", pad=0.05))

#(2) Remapped Cmap
plt.subplot(2, 1, 2)
test_plot1=plt.imshow(test_data,cmap=remapped_cmap ,interpolation='bicubic')
plt.title("Remapped Cmap")
divider = make_axes_locatable(plt.gca())
plt.colorbar(test_plot1,orientation='vertical', cax=divider.append_axes("right", size="5%", pad=0.05))

plt.subplots_adjust(hspace=.3)

#Saving plot
plt.savefig("test_fig.png",bbox_inches='tight')
