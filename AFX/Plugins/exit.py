import AFX
import sys

class module(AFX.AFXVisualPlugin):
	def __init__(self):
		self.long_name = "Exit AFX"
		self.short_name = "Exit"
		self.description = "Quits AFX and gets you out of this hell..."

		self.icon = "exit.png"	

	def call(self, widget=None, data=None):
		sys.exit()

