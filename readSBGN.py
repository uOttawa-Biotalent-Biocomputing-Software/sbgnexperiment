#LIST THE GLHPYS AND ARCS COMPONENTS IN SBGN FILE

import libsbgnpy.libsbgn as libsbgn
from libsbgnpy.libsbgnTypes import Language, GlyphClass, ArcClass, Orientation
from libsbgnpy import utils
import os.path

#READ SBGN FILE

filename = raw_input("Enter the name of the existing SBGN file: ")
if ".sbgn" not in filename:
	filename = filename + ".sbgn"	

exist = os.path.isfile(filename)

while exist==False:
	filename = raw_input("The file does not exist, please try again: ")
	if ".sbgn" not in filename:
		filename = filename + ".sbgn"
	exist = os.path.isfile(filename)

sbgn = utils.read_from_file(filename)
print sbgn
print


#ITERATING OVER ARCS&GLYPHS
map = sbgn.get_map()

glyphs = map.get_glyph()
for g in glyphs:
    cls = g.get_class()
    print cls, g.get_id()
    label = g.get_label()
    if cls == 'simple chemical':
        print 'label: ', label.get_text()

    if cls == 'process':
        for p in g.get_port():
            print 'port ', p.get_id(), p.get_x(), p.get_y()

    box = g.get_bbox()
    utils.print_bbox(box)
    print

arcs = map.get_arc()
for a in arcs:
    print a.get_class(), a.get_source(), a.get_target(), a.get_id()
    start = a.get_start()
    print start.x, start.y
    end = a.get_end()
    print end.x, end.y