import AFX

class module(AFX.AFXFileAppPlugin):
	def __init__(self):
		self.long_name = "Sega Genesis"
		self.short_name = "Genesis"
		self.exec_path = "/usr/games/bin/gens"
		self.exec_opts = "--fs-mode"
		self.description = "Play games from the 16-bit powerhouse Sega Genesis"
		self.dir_path = "/roms/genesis_roms/"
		self.icon = "genesis.png"
		
		self.init_window()
