import AFX

class module(AFX.AFXFileAppPlugin):
	def __init__(self):
		self.long_name = "Super Nintendo Entertainment System"
		self.short_name = "SNES"
		self.exec_path = "/usr/games/bin/snes9x"
		self.description = "Play games from the Super Nintendo Entertainment System."
		self.dir_path = "/roms/snes_roms"
		self.icon = "snes.png"
		
		self.init_window()
