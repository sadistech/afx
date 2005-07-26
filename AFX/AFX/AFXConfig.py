import sys
from core.AFXConf import *

conf_path = "afx.conf"

if (len(sys.argv) == 2):
	conf_path = sys.argv[1]

conf = AFXConf()
conf.init_from_file(conf_path)

