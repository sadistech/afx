import pygtk
import gtk
from AFXPlugin import *
from AFX.AFXWindow import *
from AFXVisualPlugin import *

class AFXWindowedPlugin(AFXVisualPlugin):
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

	def call(self, widget=None, data=None):
		"""
		override's AFXVisualPlugin's call()
		shows the window.
		"""
		print "showing %s's window!" % self.short_name
		self.window.show()
