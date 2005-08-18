from AFXVisualPlugin import *

class AFXAppPlugin(AFXVisualPlugin):
	"""
	AFXAppPlugin
	
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

	def launch_app(self):
		"""
		runs this plugin.
		"""

		import os 						# for popen()
		from AFX.AFXConfig import conf 	# for the afxexec bin_name

		# build the os.popen() command string.
		# 	the process is launched by the exec_bin (afxexec)
		#	see afxexec for usage details
		my_exec = "%s/%s %s" % (conf.read('bin_path'), conf.read('exec_bin_name'), self.get_exec())

		os.popen(my_exec)
