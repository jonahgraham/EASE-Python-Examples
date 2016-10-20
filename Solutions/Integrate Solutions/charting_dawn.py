include('workspace://Utilities/dawnplotting.py')
import scisoftpy as dnp


t = dnp.arange(0.0, 2.0, 0.01)
s = dnp.sin(2 * dnp.pi * t)
dnp.plot.line(t, s)
ps = dnp.plot.getPlottingSystem()
ps.setTitle("EclipseCon France Demo")