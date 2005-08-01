import AFX
import sys

class module(AFX.AFXModule):
	def __init__(self):
		AFX.AFXModule.__init__(self)

		self.long_name = "Exit AFX"
		self.short_name = "Exit"
		self.description = "Quits AFX and gets you out of this hell..."

		self.icon = "exit.png"	

	def run(self, widget=None, data=None):
		sys.exit()

	def run_end(self):
		print "%s finished!" % self.short_name
