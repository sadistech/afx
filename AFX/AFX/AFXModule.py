## AFXModule
##
## Base class for all AFXModules

class AFXModule:
	long_name 		= ""
	short_name 		= ""
	description 	= ""
	
	def __init__(self):
		pass
	
	def run(self, widget=None, data=None):
		pass
	
	def receive_event(self, event):
		## for receiving events from the main program
		## (not implemented, yet... hehe)
		pass
