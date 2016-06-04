import numpy as np
loadModule('/Charting')  # import matplotlib.pyplot as plt
include('workspace://Utilities/java_array.py')

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

plot(java_array(t, fqn="double"), java_array(s, fqn="double"))

setXLabel('time (s)')
setYLabel('voltage (mV)')
setPlotTitle('About as simple as it gets, folks')
showGrid(True)
exportGraph("test.png", True)
# auto shown, so not plt.show() equivalent
