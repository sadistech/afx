import AFX

class module(AFX.AFXFileApplication):
	def __init__(self):
		AFX.AFXFileApplication.__init__(self)
		self.long_name = "Super Nintendo Entertainment System"
		self.short_name = "SNES"
		self.exec_path = "/usr/games/bin/snes9x"
		self.description = "Play games from the Super Nintendo Entertainment System."
		self.dir_path = "/roms/snes_roms"
		
		self.init_window()

	def run_start(self):
		print "ok, %s is gonna run..." % self.short_name

	def run_end(self):
		print "%s finished!" % self.short_name
