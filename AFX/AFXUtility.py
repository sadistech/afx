"""
utility functions for AFX
"""
import pygtk
import gtk

def caseIndependentSort(a, b):
	"""
	used for List.sort() functions
	sorts without attention to case
	"""
	
	a, b = a.lower(), b.lower()
	return cmp(a, b)

def RGBColor(r=0, g=0, b=0):
	"""
	returns a gtk.gdk.Color with 100% opacity.
	r, g, b values 0->255
	since gtk.gdk.Color uses values from 0->65535, we must do some maths.
	"""
	return gtk.gdk.Color(r*256, g*256, b*256, 0)

def update_ui():
	"""
	updates the UI (for drawing things when not in the main() loop)
	"""
	while gtk.events_pending():
		gtk.main_iteration(gtk.FALSE)
