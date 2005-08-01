#! /usr/bin/env python

print "Welcome to AFX\n\n"

import pygtk
import gtk
import sys
from AFX.GUI.AFXMainWindow import *
from AFX.GUI.AFXLoadingWindow import *
from AFX.GUI.AFXView import *

import AFX.AFXConfig as AFXConfig

class App:
	def destroy(self, widget, data=None):
		self.main_window.destroy(widget)
		gtk.main_quit()
		sys.exit()

	def __init__(self):
		self.main_window = AFXMainWindow(gtk.WINDOW_TOPLEVEL)
		
		self.load_modules() # load some modules, yay!
		
		self.main_window.show()

	def load_modules(self):
		loading_window = AFXLoadingWindow()

		loading_window.show()
		loading_window.update_status("Loading modules...")
	
		print "\nLoading modules..."
		import Modules
		
		for mod in Modules.module_list:
			loading_window.update_status("Loading: %s" % mod.short_name)

		loading_window.destroy(None)
		self.main_window.module_view = AFXView(Modules.module_list)
		self.main_window.add(self.main_window.module_view)
		self.main_window.module_view.show()

		
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

