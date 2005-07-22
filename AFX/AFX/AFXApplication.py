## AFXApplication
##
## A module that executes a separate process 
##	which is managed by the AFXRuntime

from AFXModule import *

class AFXApplication(AFXModule):
	exec_path = ""	# the path of the executable
	exec_opts = ""	# any options that are going to be passed to the executable
	
	def get_exec(self):
		# returns the string needed to execute this application
		return "%s %s" % (self.exec_path, self.exec_opts)

	def run_start(self):
		pass

	def run_end(self):
		pass
