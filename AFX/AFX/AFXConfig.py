"""
AFXConfig

Module for managing the main configuration file

Instantiates an AFXConf
Checks the commandline for the main application (sys.argv) for a conf file argument (the first argument)
Uses sys.argv[1] if it's available, otherwise reads afx.conf
"""

import sys
from core.AFXConf import *

conf_path = "afx.conf" # default value...

if (len(sys.argv) >= 2):
	conf_path = sys.argv[1]

print "Reading conf: %s" % conf_path
conf = AFXConf()

try:
	conf.init_from_file(conf_path)
except:
	print "a fatal error has occurred. conf file not found. AFX must close."
	sys.exit()
