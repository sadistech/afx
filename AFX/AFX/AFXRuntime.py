def run_plugin(plugin):
	"""
	function for running a plugin that requires an application.

	this uses afx_bin/afxexec to launch a new process.
	see docs on afxexec on how it works.
	
	TODO:
		the architecture of this whole thing needs to be rethought/ recoded.
		perhaps it should be implemented into AFXApplication.
	"""
	print "run_plugin(%s)\n" % plugin.short_name

	import os
	from AFXConfig import conf

	my_exec = "%s/%s %s" % (conf.read('bin_path'), conf.read('exec_bin_name'), plugin.get_exec())

	print "my_exec: %s" % my_exec

	plugin.run_start()

	os.popen(my_exec)

	plugin.run_end()

	#print o.read()
