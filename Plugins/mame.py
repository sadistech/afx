import AFX

class module(AFX.AFXFileAppPlugin):
	def __init__(self):
		self.long_name = "Multiple Arcade Machine Emulator"
		self.short_name = "MAME"
		self.exec_path = "/usr/games/bin/xmame"
		self.exec_opts = "-jdev /dev/input/js0 -jt 1 -as -s 2 -dp alsa -smp alsa"
		self.description = "Play a huge array of classic arcade games!"
		self.dir_path = "/roms/mame_roms"
		self.icon = "mame.png"

		self.init_window()

