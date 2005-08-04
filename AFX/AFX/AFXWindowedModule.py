import pygtk
import gtk
from AFXModule import *
from AFXWindow import *

class AFXWindowedModule(AFXModule):
	"""
	AFXWindowedModule

	A module that contains a graphical interface
		it has a window for doing things with it.
	Most modules will be WindowedModules.
	"""
	
	window = None
	
	def init_window(self):
		"""
		initialize the window of the module.
		"""
		self.window = AFXWindow()

	def run(self, widget=None, data=None):
		print "%s is gonna run!" % self.short_name
		self.window.show()
