"""
AFXCommandline.py

everything that's needed to parse the commandline options and get everything ready.
"""

import sys
from AFXConf import *

global cli_conf
cli_conf = AFXConf() #placeholder for future commandline conf overrides...

# the current command:
global cur_command
cur_command = 1 # start it on the first argument (0 is the app name)

# utility methods
def next_command():
	"""
	returns the next commandline argument and increments the cur_command value
	"""
	global cur_command
	cur_command += 1
	cmd = sys.argv[cur_command]
	return cmd

def peek_command(offset=0):
	"""
	used for looking at commandline arguments
	returns the next argument if offset is zero
	otherwise returns the nth command coming up.
	"""
	global cur_command
	return sys.argv[cur_command + offset + 1]

# begin command functions...

def set_conf():
	"""
	sets the conf file.
	gets called when the parser encounters the set_conf command
	fetches the following command and sets conf_file to it.
	"""
	global conf_path
	conf_path = next_command()

# the commands that the parser can parse...
commands = {
	'-c'			: set_conf,
	'--set-conf'	: set_conf
	}
	
def parse_commands():
	"""
	iterates through the commandline arguments
	compares them to keys in the commands variable (see above) and executes the necessary command
	"""

	global cur_command

	while (cur_command < len(sys.argv)):
		try:
			# attempt the execute the command...
			commands[sys.argv[cur_command]]()
		except:
			# an error!
			# for now, we're just gonna ignore errors, but print a warning.
			print "WARNING! Unknown argument: %s" % sys.argv[cur_command]

		cur_command += 1
