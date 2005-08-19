from AFX.AFXConfig import *

plugin_list = []
loading_window = None

def load_plugin(plug_name):
	"""
	updates the loading_window (see AFXLoadingWindow.py) if it has been set
	imports plugins.
	
	TODO: this should actually have a plugin queue that gets initialized, then told to load the queue later. That way, we can import this plugin without re-importing all of the modules.
	"""
	if (loading_window != None):
		loading_window.update_status("Loading: %s" % plug_name)
		
	plugin = __import__("%s.%s" % (conf.read("plugin_dir_name") , plug_name))
	plugin = getattr(plugin, plug_name)
	plugin_list.append(plugin.module())

def load_plugins():
	"""
	the ghetto plugin queue
	"""
	load_plugin("nes")
	load_plugin("snes")
	load_plugin("mame")
	load_plugin("genesis")
	load_plugin("exit")


# this has been commented out and is handled from the place where 'import plugins' is called.
#load_modules()

# standard utility functions:

def get_plugin(index):
	"""
	pointless function that returns the plugin located at index
	"""
	return plugin_list[index]

def get_typed_plugins(type):
	"""
	returns a list of all plugins of type 'type' from plugin_list
	"""
	
	l = []
	for p in plugin_list:
		if (isinstance(p, type)):
			l.append(p)

	return l

# some extra text-based functions...

def print_plugins():
	"""
	prints a list of the plugins by plugin.long_name
	"""
	i = 0
	for item in plugin_list:
		print "%d %s" % (i, item.long_name)
		i += 1

def print_plugin_info(index):
	"""
	debugging function that prints verbose info about a plugin.
	this would probably be more useful (and less prone to becoming obsolete) if it used some object introspection instead of pre-set stuff.
	"""
	print "Short Name:\t%s" % plugin_list[index].short_name
	print "Long Name:\t%s" % plugin_list[index].long_name
	print "Description:\t%s" % plugin_list[index].description
	print "Exec Path:\t%s" % plugin_list[index].exec_path
	print "Exec Opts:\t%s" % plugin_list[index].exec_opts
	print ""
