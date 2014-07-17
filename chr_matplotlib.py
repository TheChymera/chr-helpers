__author__="Paul H, Horea Christian"
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid


def auto_remap(data):
	start=0
	midpoint=0.5
	stop=1.0
	if np.nanmin(data) >= 0:
		raise ValueError('You do not need to rescale your cmap to center zero.')    
	if np.nanmax(data) > abs(np.nanmin(data)):
		start = (np.nanmax(data)-abs(np.nanmin(data)))/(2*np.nanmax(data))
		midpoint = abs(np.nanmin(data))/(np.nanmax(data)+abs(np.nanmin(data)))
		stop = 1.0
	if np.nanmax(data) == abs(np.nanmin(data)):
		start = 0
		midpoint = 0.5
		stop = 1.0
	if np.nanmax(data) < abs(np.nanmin(data)):
		start = 0
		midpoint = abs(np.nanmin(data))/(np.nanmax(data)+abs(np.nanmin(data)))
		stop = (abs(np.nanmin(data))-np.nanmax(data))/(2*abs(np.nanmin(data)))
	return start, midpoint, stop


def remappedColorMap(cmap, data=False, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
	'''
	Function to offset the median value of a colormap, and scale the
	remaining color range. Useful for data with a negative minimum and
	positive maximum where you want the middle of the colormap's dynamic
	range to be at zero.

	Input
	-----
	cmap : The matplotlib colormap to be altered
	data: You can provide your data as a numpy array, and the following
		operations will be computed automatically for you.
	start : Offset from lowest point in the colormap's range.
		Defaults to 0.0 (no lower ofset). Should be between
		0.0 and 0.5; if your dataset vmax <= abs(vmin) you should leave 
		this at 0.0, otherwise to (vmax-abs(vmin))/(2*vmax) 
	midpoint : The new center of the colormap. Defaults to 
		0.5 (no shift). Should be between 0.0 and 1.0; usually the
		optimal value is abs(vmin)/(vmax+abs(vmin)) 
	stop : Offset from highets point in the colormap's range.
		Defaults to 1.0 (no upper ofset). Should be between
		0.5 and 1.0; if your dataset vmax >= abs(vmin) you should leave 
		this at 1.0, otherwise to (abs(vmin)-vmax)/(2*abs(vmin)) 
	'''
    
	if isinstance(data, np.ndarray):
		start, midpoint, stop = auto_remap(data)
    
    	cdict = {
    		'red': [],
    		'green': [],
    		'blue': [],
    		'alpha': []
    	}

    	# regular index to compute the colors
    	reg_index = np.hstack([
    			np.linspace(start, 0.5, 128, endpoint=False), 
    			np.linspace(0.5, stop, 129)
    	])

    	# shifted index to match the data
    	shift_index = np.hstack([
    			np.linspace(0.0, midpoint, 128, endpoint=False), 
    			np.linspace(midpoint, 1.0, 129)
    	])

    	for ri, si in zip(reg_index, shift_index):
    		r, g, b, a = cmap(ri)

        	cdict['red'].append((si, r, r))
        	cdict['green'].append((si, g, g))
        	cdict['blue'].append((si, b, b))
        	cdict['alpha'].append((si, a, a))

    	newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    	plt.register_cmap(cmap=newcmap)

	return newcmap
