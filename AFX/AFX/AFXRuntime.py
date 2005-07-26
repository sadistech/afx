def run_module(module):
	print "run_module(%s)\n" % module.short_name

	import os
	from AFXConfig import conf

	#my_exec = "%s/%s %s %s %s" % (AFXConf.bin_path, AFXConf.exec_bin_name, module.exec_path, module.exec_opts, module.file_name)

	my_exec = "%s/%s %s" % (conf.read('bin_path'), conf.read('exec_bin_name'), module.get_exec())

	print "my_exec: %s" % my_exec

	module.run_start()

	os.popen(my_exec)

	module.run_end()

	#print o.read()
