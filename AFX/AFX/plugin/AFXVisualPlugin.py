from AFXPlugin import *

class AFXVisualPlugin(AFXPlugin):
	"""
	Plugin that is selectable from the application
	It's actually visible, like.
	"""

	long_name 		= ""
	description 	= ""

	def call(self, widget=None, data=None):
		"""
		Gets called when the plugin is selected in the main window.
		"""
		pass
