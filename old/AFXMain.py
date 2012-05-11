print "Welcome to AFX\n\n"

print "Loading modules..."
import Modules

print "Loaded Modules:"
for item in Modules.module_list:
	print "\t%s (%s)" % (item.short_name, item.long_name)

import AFX

#ok, let's just loop and take commands and stuff for now...
print "Type ? for help"
s = ""
while (s != 'q'):
	s = raw_input("> ")
	if (s == 'l'):
		Modules.print_modules()
	elif (s == '?'):
		print "Commands:"
		print "\tl: list modules"
		print "\ti: module info"
		print "\td: reload modules"
		print "\tr: run module"
		print "\t?: help"
		print "\tq: quit\n"
	elif (s == 'i'):
		s = input("Module #: ")
		Modules.print_module_info(s)
	elif (s == "d"):
		reload(Modules)
	elif (s == "r"):
		i = input("Module #: ")
		file_name = raw_input("Filename: ")
		Modules.get_module(i).file_name = file_name
		AFX.run_module(Modules.get_module(i))
	elif (s == "q"):
		break
	elif (s == ""):
		# do nothing...
		pass
	else:
		print "Unknown command (%s)" % s

	print ""
#Modules.module_list[2].file_name = "/home/spike/Mame\ Roms\ S-Z/sf2.zip"

#AFX.run_module(Modules.module_list[2])

print "ok, let's see... are we done?"
