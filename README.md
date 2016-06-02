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
https://www.dropbox.com/sh/5cwzbzrsebdyd6x/AACRc-p3VpyJCqU4Yqtdp27Ca?dl=0

[![Install EASE](extras/installease.png)](https://www.dropbox.com/sh/5cwzbzrsebdyd6x/AACRc-p3VpyJCqU4Yqtdp27Ca?dl=0)

### Manual Set-up 
If for whatever reason, you are unable to use the all-in-one product installer, here are manual steps to obtain an equivalent set-up. 

* Install [Eclipse IDE for Committers Mars.2] (https://www.eclipse.org/downloads/packages/eclipse-ide-eclipse-committers-452/mars2)
* Download & install [EASE for EclipseCon France] (https://www.dropbox.com/sh/5cwzbzrsebdyd6x/AACRc-p3VpyJCqU4Yqtdp27Ca?dl=0)
* Install [PyDev] (http://www.pydev.org/download.html). This step is optional, but provides a nice editor for writing Python scripts. 

Configuration
---------------
EASE will use Python off your System Path, please ensure a valid version of Python can be found off the System Path.


