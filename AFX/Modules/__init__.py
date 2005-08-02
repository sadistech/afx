module_list = []
loading_window = None

def load_module(mod_name):
	"""
	updates the loading_window (see AFXLoadingWindow.py) if it has been set
	imports modules.
	
	TODO: this should actually have a module queue that gets initialized, then told to load the queue later. That way, we can import this Module (maybe I should rename Modules to plugins to avoid confusion?) without re-importing all of the modules.
	"""
	if (loading_window != None):
		loading_window.update_status("Loading: %s" % mod_name)
		
	mod = __import__("Modules.%s" % mod_name)
	mod = getattr(mod, mod_name)
	module_list.append(mod.module())

def load_modules():
	"""
	the ghetto module queue
	"""
	load_module("nes")
	load_module("snes")
	load_module("mame")
	load_module("exit")


#load_modules()

# standard utility functions:

def get_module(index):
	"""
	pointless function that returns the module located at index
	"""
	return module_list[index]

# some extra text-based functions...

def print_modules():
	"""
	prints a list of the modules by module.long_name
	"""
	i = 0
	for item in module_list:
		print "%d %s" % (i, item.long_name)
		i += 1

def print_module_info(index):
	"""
	debugging function that prints verbose info about a module.
	this would probably be more useful (and less prone to becoming obsolete) if it used some object introspection instead of pre-set stuff.
	"""
	print "Short Name:\t%s" % module_list[index].short_name
	print "Long Name:\t%s" % module_list[index].long_name
	print "Description:\t%s" % module_list[index].description
	print "Exec Path:\t%s" % module_list[index].exec_path
	print "Exec Opts:\t%s" % module_list[index].exec_opts
	print ""
