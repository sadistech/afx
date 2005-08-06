from AFXPlugin import *

class AFXApplication(AFXPlugin):
	"""
	AFXApplication
	
	A plugin that executes a separate process 
		which is managed by the AFXRuntime
	"""
	
	exec_path = ""	# the path of the executable
	exec_opts = ""	# any options that are going to be passed to the executable
	
	def get_exec(self):
		"""
		returns the string needed to execute this application
		
		exec_path exec_opts
		"""
		return "%s %s" % (self.exec_path, self.exec_opts)

	def run_start(self):
		"""
		event for when this AFXApplication is about to run
		called right before execution
		"""
		pass

	def run_end(self):
		"""
		event for when this AFXApplication is done running
		called right after execution finishes (when the process returns)
		"""
		pass
