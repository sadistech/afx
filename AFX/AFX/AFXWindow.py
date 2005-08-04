import pygtk
import gtk

class AFXWindow(gtk.Window):
	"""
	a gtk.Window that's initialized for AFX
	it's full screen and has specific behavior and appearance.
	"""
	main_box = None
	
	def __init__(self, type=gtk.WINDOW_TOPLEVEL):
		gtk.Window.__init__(self, type) #do the super thing, first

		self.set_title("AFX")
		#self.set_decorated(0)
		self.move(0,0)

		s_width = gtk.gdk.screen_width()
		s_height = gtk.gdk.screen_height()

		self.resize(500, 500) #temporarily, so we can still work

		self.connect("destroy", self.destroy)
		
	def destroy(self, widget, data=None):
		self.hide()
		
		gtk.Window.destroy(self)
