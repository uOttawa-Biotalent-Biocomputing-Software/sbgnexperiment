###RENDER SBGN FILE###


from libsbgnpy import render, utils
import os.path

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

pngname = ""
for w in filename:
	if w == '.':
		break;
	else:
		pngname += w
pngname += ".png"

render.render_sbgn(sbgn, pngname)

