import pygtk
import gtk
import pango
from AFX.plugin.AFXVisualPlugin import *

class AFXView(gtk.DrawingArea):
	plugin_manager = None
	images = []
	selection = 0 # the currently selected item

	def __init__(self, plugin_manager):
		"""
		initializes the AFXView with a plugin_manager (from the Modules module)
		"""

		gtk.DrawingArea.__init__(self)
		self.images = []
		self.plugin_manager = plugin_manager

		# set up the images
		for m in plugin_manager.get_typed_plugins(AFXVisualPlugin):
			i = gtk.Image()
			i.set_from_file("icons/%s" % m.icon)
			self.images.append(i)
		
		# connect the drawing method
		self.connect("expose_event", self.paint)

		# connect the key trapping method...
		self.set_flags(gtk.CAN_FOCUS)
		self.connect("key_press_event", self.keydown)

	def keydown(self, widget, event):
		"""
		used for capturing keyboard events
		"""
		if (event.keyval == 65361): # left
			self.prev()
		elif (event.keyval == 65363): # right
			self.next()
		elif (event.keyval == 65293): # return
			self.run_selected()
		else:
			print "debug: keyval=%d" % event.keyval

	def next(self):
		"""
		increments the selection and redraws the view
		"""
		self.selection += 1
		
		if (self.selection == len(self.images)):
			self.selection = 0
	
		self.paint(self, None)

	def prev(self):
		"""
		decrements the selection and redraws the view
		"""
		self.selection -= 1
		
		if (self.selection < 0):
			self.selection = len(self.images) - 1
			
		self.paint(self, None)

	def run_selected(self):
		"""
		executes the currently selected plugin
		"""
		self.get_plugin(self.selection).call()
		
	def get_plugin(self, index):
		"""
		returns the visual plugin with index
		"""
		return self.plugin_manager.get_typed_plugins(AFXVisualPlugin)[index % self.get_plugin_count()]

	def get_plugin_count(self):
		return len(self.plugin_manager.get_typed_plugins(AFXVisualPlugin))

	def get_image(self, index):
		"""
		returns the image with index
		"""
		#if (index < 0):
		#return self.images[-(index % len(self.images))]
		#else:
		return self.images[index % len(self.images)]

	def paint(self, widget, event):
		"""
		draws the view with all icons and whatnot
		primary icon is 256px x 256px sandwiched between 2 secondary icons @ 128px square, then sandwiched between 4 (2 on each side) icons @ 64px. All icons are drawn 32px apart.
		"""
		#gc = self.window.new_gc()
		(w, h) = self.window.get_size()

		gb = gtk.gdk.Pixmap(self.window, w, h, -1) # graphic buffer
		gc = gb.new_gc(line_width=2, join_style=gtk.gdk.JOIN_ROUND)

		#print "paint: self.images.count: %d" % len(self.images)

		if (len(self.images) == 0):
			return
	
		#first, initialize the graphics by filling the buffer with black
		gc.set_rgb_fg_color(gtk.gdk.Color(0, 0, 0))
		gb.draw_rectangle(gc, gtk.TRUE, 0, 0, w, h)
	
		# draw the dark gray bar...
		gc.set_rgb_fg_color(gtk.gdk.Color(25600, 25600, 25600))
		gb.draw_rectangle(gc, gtk.TRUE, 0, (h / 2) - (384 / 2), w, 384)
		
		# draw primary (selected) icon
		gc.set_rgb_fg_color(gtk.gdk.Color(30000, 30000, 30000))
		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) - 128, (h / 2) - 128, 256, 256)
		pb = self.get_image(self.selection).get_pixbuf()
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) - 128, (h / 2) - 128, 256, 256)

		# draw secondary box
		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) + 128 + 32, (h / 2) - 64, 128, 128)
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, gtk.TRUE, 8, 128, 128)
		self.get_image(self.selection + 1).get_pixbuf().scale(pb, 0, 0, 128, 128, 0, 0, .5, .5, gtk.gdk.INTERP_BILINEAR)
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) + 128 + 32, (h / 2) - 64, 128, 128)
		
		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) - 128 - 32 - 128, (h / 2) - 64, 128, 128)
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, gtk.TRUE, 8, 128, 128)
		self.get_image(self.selection - 1).get_pixbuf().scale(pb, 0, 0, 128, 128, 0, 0, .5, .5, gtk.gdk.INTERP_BILINEAR)
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) - 128 - 32 - 128, (h / 2) - 64, 128, 128)

		# draw last boxes...
		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) + 128 + 128 + 64, (h / 2) - 32, 64, 64)
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, gtk.TRUE, 8, 64, 64)
		self.get_image(self.selection + 2).get_pixbuf().scale(pb, 0, 0, 64, 64, 0, 0, .25, .25, gtk.gdk.INTERP_BILINEAR)
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) + 128 + 128 + 64, (h / 2) - 32, 64, 64)
		
		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) + 128 + 128 + 96 + 64, (h / 2) - 32, 64, 64)
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, gtk.TRUE, 8, 64, 64)
		self.get_image(self.selection + 3).get_pixbuf().scale(pb, 0, 0, 64, 64, 0, 0, .25, .25, gtk.gdk.INTERP_BILINEAR)
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) + 128 + 128 + 96 + 64, (h / 2) - 32, 64, 64)

		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) - 128 - 128 - 64 - 64, (h / 2) - 32, 64, 64)
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, gtk.TRUE, 8, 64, 64)
		self.get_image(self.selection - 2).get_pixbuf().scale(pb, 0, 0, 64, 64, 0, 0, .25, .25, gtk.gdk.INTERP_BILINEAR)
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) - 128 - 128 - 64 - 64, (h / 2) - 32, 64, 64)
		
		#gb.draw_rectangle(gc, gtk.FALSE, (w / 2) - 128 - 128 - 96 - 64 - 64, (h / 2) - 32, 64, 64)
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, gtk.TRUE, 8, 64, 64)
		self.get_image(self.selection - 3).get_pixbuf().scale(pb, 0, 0, 64, 64, 0, 0, .25, .25, gtk.gdk.INTERP_BILINEAR)
		gb.draw_pixbuf(gc, pb, 0, 0, (w / 2) - 128 - 128 - 96 - 64 - 64, (h / 2) - 32, 64, 64)
		
		# draw the selection's long_name
		l = pango.Layout(self.get_pango_context())
		l.set_markup("<span size='36000' weight='ultrabold'>%s</span>" % self.get_plugin(self.selection).long_name)
		
		# set the foreground colour to white...
		gc.set_rgb_fg_color(gtk.gdk.Color(65535, 65535, 65535))
		
		(lw, lh) = l.get_pixel_size() #layout width and height
	
		# draw the long_name
		gb.draw_layout(gc, (w / 2 - lw / 2), 72, l)

		# draw the description!
		l = pango.Layout(self.get_pango_context())
		l.set_markup("<span size='24000' style='italic'>%s</span>" % self.get_plugin(self.selection).description)
		l.set_wrap(pango.WRAP_WORD) 	# set it to wrap on word boundries
		l.set_width(w * 500) 				# set the wrap-width to half the window's width
		
		# set the foreground colour to light gray...
		gc.set_rgb_fg_color(gtk.gdk.Color(45000, 45000, 45000))

		(lw, lh) = l.get_pixel_size() #description width and height

		#draw the damned description!
		gb.draw_layout(gc, (w / 2 - lw / 2), h - 128, l)
		

		#flip the offscreen buffer onto the drawable! yay! flickerless drawing!
		self.window.draw_drawable(self.window.new_gc(), gb, 0, 0, 0, 0, w, h)
