#! /usr/bin/env python

print "Welcome to AFX\n\n"

# first thing's first... let's parse the commandline options...
import AFX.core.AFXCommandline as CLI
CLI.parse_commands()

# then, let's read the conf...
import AFX.AFXConfig as AFXConfig
# if the commandline overrided the conf file, let's read that one.
if (CLI.__dict__.has_key("conf_path")):
	AFXConfig.conf_path = CLI.conf_path

# read the conf file
AFXConfig.init()

# now, let's start initializing the program...

import pygtk
import gtk
import sys
from AFX.GUI.AFXMainWindow import *
from AFX.GUI.AFXLoadingWindow import *
from AFX.GUI.AFXView import *


class App:
	def destroy(self, widget, data=None):
		self.main_window.destroy(widget)
		gtk.main_quit()
		sys.exit()

	def __init__(self):
		self.main_window = AFXMainWindow(gtk.WINDOW_TOPLEVEL)
		
		self.load_plugins() # load some plugins, yay!
		
		self.main_window.show()

	def load_plugins(self):
		loading_window = AFXLoadingWindow()

		loading_window.show()
		loading_window.update_status("Loading plugins...")
	
		print "\nLoading plugins..."
		import Plugins

		Plugins.loading_window = loading_window
		Plugins.load_plugins()
		
		#for mod in Modules.plugin_list:
		#	loading_window.update_status("Loading: %s" % mod.short_name)

		loading_window.update_status("Initializing main view...")

		self.main_window.plugin_view = AFXView(Plugins)
		self.main_window.add(self.main_window.plugin_view)
		self.main_window.plugin_view.show()

		loading_window.destroy(None)
	
	def update_description(self, widget, event, desc):
		pass
		self.main_window.description.set_markup("<i>%s</i>" % desc)
	
	def update_full_name(self, widget, event, full_name):
		pass
		#self.main_window.full_name.set_markup("<span size='xx-large' weight='bold' foreground='white' background='black'>%s</span>" % full_name)

	def main(self):
		gtk.main()

	
if __name__ == "__main__":
	app = App()
	app.main()

