import sys
sys.path.append('''C:\data\Projects\NOBUGS\plugins\uk.ac.diamond.scisoft.python_1.3.0''')
import scisoftpy as dnp
print(dir(dnp.rpc))
dnp.plot.setremoteport(51046)

t = dnp.arange(0.0, 2.0, 0.01)
s = dnp.sin(2 * dnp.pi * t)
dnp.plot.line(t, s)
ps = dnp.plot.getPlottingSystem()
print type(ps)
ps.setTitle("EclipseCon France Demo")
