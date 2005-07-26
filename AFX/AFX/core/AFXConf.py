import re

class AFXConfig:
	data = {}

	def __init__(self):
		self.data = {}

	def read(self, key):
		return self.data[key]

	def write(self, key, value):
		self.data[key] = value

	def rename(self, key, new_key):
		self.data[new_key] = self.data[key]
		del self.data[key]
	
	def keys(self):
		return self.data.keys()

	def init_from_file(self, file_path):
		f = open(file_path, "r")
		lines = f.readlines()
		for line in lines:
			if (line[0] != "#"): 				# if it's not a comment...
				if (re.match(r"\w", line)): 	# if the line's not blank
					print "processed: %s" % line
					m = re.match(r"^([\S]+)\s+(.+)$", line)
					self.write(m.group(1), m.group(2))
