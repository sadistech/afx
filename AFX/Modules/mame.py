import AFX

class module(AFX.AFXFileApplication):
	def __init__(self):
		AFX.AFXFileApplication.__init__(self)

		self.long_name = "Multiple Arcade Machine Emulator"
		self.short_name = "MAME"
		self.exec_path = "/usr/games/bin/xmame"
		self.exec_opts = "-jdev /dev/input/js0 -jt 1 -as -s 2 -dp alsa -smp alsa"
		self.description = "Play a huge array of classic arcade games!"
		self.dir_path = "/home/spike/Mame Roms S-Z"

		self.init_window()

	def run_start(self):
		print "ok, %s is gonna run..." % self.short_name
	
	def run_end(self):
		print "%s finished!" % self.short_name
