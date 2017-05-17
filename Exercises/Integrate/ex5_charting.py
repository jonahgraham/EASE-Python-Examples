# 1. import numpy 
# 2. load charting module
include('workspace://Utilities/java_array.py')

# numpy to plot sine wave
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

# how to plot array values
plot(java_array(t, fqn="double"), java_array(s, fqn="double"))

# 3. set the x axis label to time(s)
# 4. set the y axis lable to voltage(mV)
# 5. set plot title to 'As simple as it gets'
# 6. set grid to true
# 7. export the graph to test.png

# 8. BONUS: add another plot (maybe the cos equivalent of s) or change the plot on the chart
