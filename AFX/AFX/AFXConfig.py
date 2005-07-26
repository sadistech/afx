import sys
from core.AFXConf import *

conf_path = "afx.conf" # default value...

if (len(sys.argv) == 2):
	conf_path = sys.argv[1]

conf = AFXConf()

try:
	conf.init_from_file(conf_path)
except:
	print "a fatal error has occurred. conf file not found. AFX must close."
	sys.exit()
