# This file adds scisoftpy to the Python Interpreter path
# The remoteport must match the port specified on the Preferences>DAWN>Analysis RPC & RMI
# The AnalysisRPC port is the one required
import sys
sys.path.append('''C:\data\Projects\NOBUGS\plugins\uk.ac.diamond.scisoft.python_1.3.0''')
import scisoftpy as dnp  # @UnresolvedImport
dnp.plot.setremoteport(55614)

