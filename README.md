EASE Python Tutorial  
=====================
The Eclipse Advanced Scripting Environment (EASE) makes it very easy to extend and control the Eclipse IDE using the popular scripting language Python.

[Join the chat at EASE on Mattermost](https://mattermost-test.eclipse.org/eclipse/channels/ease)

This tutorial shows you how to set-up and use Python scripting with EASE.

Pre-requisites
---------------
* Java 8 with a JDK
* Python 2.7(or higher) or 3.4(or higher) installed and runnable from the path
* The NumPy Python package is required to run the NumPy part of the tutorial.

To install Python and NumPy we can recommend the Anaconda Python 3.5 distribution from:
https://www.continuum.io/downloads.

Set-up
---------------
We will be using a specific version of EASE for the tutorial, please install it from the links below.  
(The EASE nightly build is awaiting some CQs to go through the approval process)

### All-in-One Product

This is a link to a pre-built Eclipse product that consists of Eclipse IDE for Committers, EASE with Py4J and PyDEV. 

[![Install EASE](extras/installease.png)](https://www.dropbox.com/sh/5cwzbzrsebdyd6x/AACRc-p3VpyJCqU4Yqtdp27Ca?dl=0)

(For reference the product is built from https://github.com/jonahkichwacoders/org.eclipse.ease.core)

### Manual Set-up 
If for whatever reason, you are unable to use the all-in-one product installer, here are manual steps to obtain an equivalent set-up. 

* Install [Eclipse IDE for Committers Neon] (https://www.eclipse.org/downloads/packages/eclipse-ide-eclipse-committers/neonr)
* Download & install [EASE for EclipseCon France] (https://www.dropbox.com/sh/5cwzbzrsebdyd6x/AACRc-p3VpyJCqU4Yqtdp27Ca?dl=0)
* Install [PyDev] (http://www.pydev.org/download.html). This step is optional, but provides a nice editor for writing Python scripts. 

Configuration
---------------
Launch Eclipse (eclipse.exe) and switch to the Scripting perspective. If not already selected, change the script shell to 'Python Script Shell'.

By default, EASE will use Python off your System Path. If you need to specify a different Python, you can change this in Preferences->Scripting->Python Scripting->Python location.

Optionally, you can configure the PyDev interpreter to point to the same version of Python (for file editing).

Release Notes
-------------

 * 2016-07-21: Fix bug where EASE overwrote PYTHONPATH, PYTHONPATH is now extended with path to py4j-python sources
 * 2016-07-21: Merge current upstream EASE code, updated product to be based on Neon.0
 * 2016-07-01: Current version on dropbox rebuilt with new Py4J release.
