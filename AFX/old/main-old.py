import nes

mod = nes.module()

print "Loaded..."
print "\tLong Name:\t %s" % mod.long_name
print "\tShort Name:\t %s" % mod.short_name
print "\tExecutable:\t %s" % mod.exec_path
print "\tDescription:\t %s" % mod.description
print "\n"

mod.run()
