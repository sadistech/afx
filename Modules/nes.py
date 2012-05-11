import AFX

class module(AFX.AFXFileApplication):
	def __init__(self):
		AFX.AFXFileApplication.__init__(self)

		self.long_name = "Nintendo Entertainment System"
		self.short_name = "NES"
		self.exec_path = "/usr/games/bin/fceu-sdl"
		self.description = "Play games from the original Nintendo Entertainment System."
		self.dir_path = "/roms/nes_roms"
		self.icon = "nes.png"

		self.init_window()

	def run_start(self):
		print "ok, %s is gonna run..." % self.short_name

	def run_end(self):
		print "%s finished!" % self.short_name
