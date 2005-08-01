import pygtk
import gtk
import pango

class AFXView(gtk.DrawingArea):
	module_list = []
	images = []
	selection = 0 # the currently selected item

	def __init__(self, module_list):
		"""
		initializes the AFXView with a module_list (from the Modules module)
		"""

		gtk.DrawingArea.__init__(self)
		self.images = []
		self.module_list = module_list

		# set up the images
		for m in module_list:
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
		executes the currently selected module
		"""
		self.get_module(self.selection).run()
		
	def get_module(self, index):
		"""
		returns the module with index
		"""
		#if (index < 0):
		#	return self.module_list[-(index % len(self.module_list))]
		#else:
		return self.module_list[index % len(self.module_list)]

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
		
		l = pango.Layout(self.get_pango_context())
		l.set_markup("<span size='36000' weight='ultrabold'>%s</span>" % self.get_module(self.selection).long_name)
		#l.set_text("Nintendo Entertainment System")
		#l.set_alignment(pango.ALIGN_CENTER)
		#al = pango.AttrList()
		#al.insert(pango.AttrSize(72000, 0, len(l.get_text())))
		#l.set_attributes(al)
		#l.context_changed()
		
		gc.set_rgb_fg_color(gtk.gdk.Color(65535, 65535, 65535))
		(lw, lh) = l.get_pixel_size()
	
		gb.draw_layout(gc, (w / 2 - lw / 2), 72, l)
		
		self.window.draw_drawable(self.window.new_gc(), gb, 0, 0, 0, 0, w, h)
