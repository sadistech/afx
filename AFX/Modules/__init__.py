module_list = []

def load_module(mod_name):
	mod = __import__("Modules.%s" % mod_name)
	mod = getattr(mod, mod_name)
	module_list.append(mod.module())

def load_modules():
	load_module("nes")
	load_module("snes")
	load_module("mame")
	load_module("exit")
	
load_modules()

# standard utility functions:

def get_module(index):
	return module_list[index]

# some extra text-based functions...

def print_modules():
	i = 0
	for item in module_list:
		print "%d %s" % (i, item.long_name)
		i += 1

def print_module_info(index):
	print "Short Name:\t%s" % module_list[index].short_name
	print "Long Name:\t%s" % module_list[index].long_name
	print "Description:\t%s" % module_list[index].description
	print "Exec Path:\t%s" % module_list[index].exec_path
	print "Exec Opts:\t%s" % module_list[index].exec_opts
	print ""
