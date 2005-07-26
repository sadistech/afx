## AFXConf.py
## 
## a wrapper for a dictionary
## supports reading, writing and renaming keys
## also supports initializing the dictionary from a file
##
## format of an AFXConf file is:
## octothorp as the first character on a line for comments
##	later on, maybe I should implement first non-whitespace char?
## key_name value goes here
## to summarize: key name is all characters up until the first whitespace char
##	value is every character starting from the first non-whitespace character
##	after the whitespace until the end of the line (not including the \n)

import re

class AFXConf:
	data = {}	# create an empty dictionary...

	def __init__(self):
		# just initialize...
		self.data = {}

	def read(self, key):
		# reads a key and returns the value
		return self.data[key]

	def write(self, key, value):
		# sets a key to a new value.
		# key is created if it doesn't exist
		self.data[key] = value

	def rename(self, key, new_key):
		# renames a key (just in case)
		self.data[new_key] = self.data[key]
		del self.data[key]
	
	def keys(self):
		# returns a list of available keys
		return self.data.keys()

	def init_from_file(self, file_path):
		# initializes the dictionary from a file
		# see comments at top of file for conf file format
		
		f = open(file_path, "r")
		lines = f.readlines()
		for line in lines:
			if (line[0] != "#"): 				# if it's not a comment...
				if (re.match(r"\w", line)): 	# if the line's not blank
					print "processed: %s" % line
					m = re.match(r"^\s*([\S]+)\s+(.+)\n$", line)
					self.write(m.group(1), m.group(2))
