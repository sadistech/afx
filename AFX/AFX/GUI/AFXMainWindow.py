import pygtk
import gtk
from AFX.AFXWindow import *
#from AFXView import *

class AFXMainWindow(AFXWindow):
	description = None		# the module's description
	full_name = None		# the module's full name
	btn_box = None			# the box of module buttons...

	def __init__(self, type):
		AFXWindow.__init__(self, type) #do the super thing, first

		#self.main_box = gtk.VBox(gtk.TRUE, 0)

		# create the full-name widget
		#	displays the module's full name when highlighted
		#self.full_name = gtk.Label("Full Module Name")
		#self.full_name.set_use_markup(gtk.TRUE)
		#self.main_box.pack_start(self.full_name, gtk.FALSE, gtk.FALSE, 0)
		#self.full_name.show()

		# create the button bar widget
		#self.btn_box = gtk.HBox(gtk.FALSE, 0)
	
		# create the description box widget
		#	displays the module's description...
		#self.description = gtk.Label("Description")
		#self.description.set_use_markup(gtk.TRUE)
		#self.main_box.pack_start(self.description, gtk.FALSE, gtk.FALSE, 0)
		#self.description.show()
	
		#self.add(self.main_box)
		#self.main_box.show()
