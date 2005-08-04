class AFXModule:
	"""
	AFXModule
	
	Base class for all AFXModules

	TODO:
		modules need to be renamed to 'plugins' to avoid syntactical confusion between AFX and python...
	"""

	long_name 		= ""
	short_name 		= ""
	description 	= ""
	icon			= ""

	def __init__(self):
		pass
	
	def run(self, widget=None, data=None):
		"""
		Gets called when the module is selected in the main window.
		TODO:
			this should probably be only in AFXApplication, or another subclass.
				(not all modules will be runable; like any event-only module)
		"""
		pass
	
	def receive_event(self, event):
		"""
		for receiving events from the main program
		(not implemented, yet... hehe)
		"""

		pass
