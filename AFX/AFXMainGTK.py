#! /usr/bin/env python

print "Welcome to AFX\n\n"

import pygtk
import gtk
import sys
from AFX.GUI.AFXMainWindow import *
from AFX.GUI.AFXLoadingWindow import *

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
	
		print "Loading modules..."
		import Modules
		
		for mod in Modules.module_list:
			loading_window.update_status("Loading: %s" % mod.short_name)
			b = gtk.Button(mod.short_name)
			self.main_window.btn_box.pack_start(b, gtk.FALSE, gtk.FALSE, 0)
			b.connect("clicked", mod.run, "")
			b.connect("focus-in-event", self.update_description, mod.description)
			b.connect("focus-in-event", self.update_full_name, mod.long_name)
			b.show()

		loading_window.destroy(None)

	def update_description(self, widget, event, desc):
		self.main_window.description.set_markup("<i>%s</i>" % desc)
	
	def update_full_name(self, widget, event, full_name):
		self.main_window.full_name.set_markup("<span size='xx-large' weight='bold' foreground='white' background='black'>%s</span>" % full_name)

	def main(self):
		gtk.main()

	
if __name__ == "__main__":
	app = App()
	app.main()

# NOTHING TO SEE HERE....

print "Loading modules..."
import Modules

print "Loaded Modules:"
for item in Modules.module_list:
	print "\t%s (%s)" % (item.short_name, item.long_name)

import AFX

#ok, let's just loop and take commands and stuff for now...
print "Type ? for help"
s = ""
while (s != 'q'):
	s = raw_input("> ")
	if (s == 'l'):
		Modules.print_modules()
	elif (s == '?'):
		print "Commands:"
		print "\tl: list modules"
		print "\ti: module info"
		print "\td: reload modules"
		print "\tr: run module"
		print "\t?: help"
		print "\tq: quit\n"
	elif (s == 'i'):
		s = input("Module #: ")
		Modules.print_module_info(s)
	elif (s == "d"):
		reload(Modules)
	elif (s == "r"):
		i = input("Module #: ")
		file_name = raw_input("Filename: ")
		Modules.get_module(i).file_name = file_name
		AFX.run_module(Modules.get_module(i))
	elif (s == "q"):
		break
	elif (s == ""):
		# do nothing...
		pass
	else:
		print "Unknown command (%s)" % s

	print ""
#Modules.module_list[2].file_name = "/home/spike/Mame\ Roms\ S-Z/sf2.zip"

#AFX.run_module(Modules.module_list[2])

print "ok, let's see... are we done?"
