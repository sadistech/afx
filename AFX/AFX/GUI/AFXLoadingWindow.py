import pygtk
import gtk
from AFX.AFXWindow import *
import AFX

class AFXLoadingWindow(AFXWindow):
	def __init__(self):
		AFXWindow.__init__(self, gtk.WINDOW_TOPLEVEL)
		
		self.modify_bg(gtk.STATE_NORMAL, AFX.RGBColor())
		self.modify_fg(gtk.STATE_NORMAL, AFX.RGBColor(255, 255, 255))

		self.main_box = gtk.VBox(gtk.FALSE, 0)
		self.add(self.main_box)
		self.main_box.show()

		self.main_box.status_text = gtk.Label("Status...")
		self.main_box.pack_start(self.main_box.status_text, gtk.FALSE, gtk.FALSE, 0)
		self.main_box.status_text.modify_fg(gtk.STATE_NORMAL, AFX.RGBColor(255, 255, 255))
		self.main_box.status_text.show()


	def update_status(self, text):
		self.main_box.status_text.set_markup("<span size='xx-large' weight='bold'>%s</span>" % text)
		self.main_box.status_text.queue_draw()
		self.queue_draw()
		AFX.update_ui()
