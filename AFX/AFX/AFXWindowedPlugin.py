import pygtk
import gtk
from AFXPlugin import *
from AFXWindow import *

class AFXWindowedPlugin(AFXPlugin):
	"""
	AFXWindowedPlugin

	A plugin that contains a graphical interface
		it has a window for doing things with it.
	Most plugins will be WindowedPlugin.
	"""
	
	window = None
	
	def init_window(self):
		"""
		initialize the window of the plugin.
		"""
		self.window = AFXWindow()

	def run(self, widget=None, data=None):
		print "%s is gonna run!" % self.short_name
		self.window.show()
