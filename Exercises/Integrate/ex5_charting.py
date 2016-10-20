# 1. import numpy 
# 2. import dnp
include('workspace://Utilities/java_array.py')

# numpy to plot sine wave
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

# plot using dnp Plotting system