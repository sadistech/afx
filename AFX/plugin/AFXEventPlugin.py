from AFXPlugin import *
from AFX.AFXEvent import *

class AFXEventPlugin(AFXPlugin):
	"""
	Base class for plugins that receive events.
	"""
	def receive_event(self, event=None):
		"""
		receive and handle an event.
		subclasses should override this...
		"""

		pass
