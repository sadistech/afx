from AFXApplication import *
from AFXWindowedModule import *
import AFXRuntime
import os
import AFX

import pygtk
import gtk


class AFXFileApplication(AFXApplication, AFXWindowedModule):
	"""
	AFXFileApplication
	
	an AFXApplication that passes a file to the commandline.
	Also creates a filebrowser for accessing the files to pass to
		the program...

	TODO:
		Add exit button to window...
		add browsing capability (so you can sort files into folders)
		add themability (colors for the listbox, etc)
	"""
dir_path = ""		# path to the starting directory for the filebrowser
	dir_list = list()	# cached list of the directory's contents
	filename = ""		# the filename of the file to be launched...
	run = AFXWindowedModule.run
	
	def init_window(self):
		self.window = AFX.AFXWindow(gtk.WINDOW_TOPLEVEL)
		# this should be called from the subclasser's __init__() method
		# let's init the window a little more than default...
		
		self.dir_list = list() # make the dir_list an empty list
		l= os.listdir(self.dir_path)
		# let's clean out any .filename files and sort the list properly

		l.sort(AFX.caseIndependentSort)
		for item in l:
			if (item[0] != '.'): # ignore any .files
				self.dir_list.append(item)

		box = gtk.VBox(gtk.FALSE, 10)
		box.set_border_width(5)

		treestore = gtk.TreeStore(str)
		for filename in self.dir_list:
			treestore.append(None, [filename[:-4]]) # append the filename without the extension
			#print "added %s" % filename

		self.treeview = gtk.TreeView(treestore)
		self.treeview.set_headers_visible(gtk.FALSE)
		tvcolumn = gtk.TreeViewColumn('Files')
		self.treeview.append_column(tvcolumn)
		cell = gtk.CellRendererText()
		tvcolumn.pack_start(cell, True)

		tvcolumn.add_attribute(cell, 'text', 0)

		self.sw = gtk.ScrolledWindow()
		self.sw.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
		self.sw.add(self.treeview)
		box.pack_start(self.sw)
		self.sw.show()

		self.treeview.show()

		start_button = gtk.Button("START")
		box.pack_start(start_button, gtk.FALSE, gtk.FALSE, 0)
		start_button.connect("clicked", self.handle_run, None)
		
		start_button.show()
		
		box.show()
		self.window.add(box)

		print "window initialized for %s (%d files)" % (self.short_name, len(self.dir_list))

	def handle_run(self, widget, data):
		print "gonna run %s" % self.short_name

		treeselection = self.treeview.get_selection()
		(model, iter) = treeselection.get_selected()

		self.filename = self.dir_list[int(model.get_string_from_iter(iter))]

		print "rom: %s" % self.filename

		AFXRuntime.run_module(self)

	def get_exec(self):
		return "%s %s \"%s/%s\"" % (self.exec_path, self.exec_opts, self.dir_path, self.filename)
