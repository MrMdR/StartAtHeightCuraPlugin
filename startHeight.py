#Name: Start height
#Info: Start the printer at a certain height in comparison to the home height.
#Depend: GCode
#Type: postprocess
#Param: startHeight(float:3.0) Start height (mm)

## Written by Mark de Reijer, mailme@markdereijer.nl
## For FabLab Breda

#history / changelog:
#V1.0.0: Made the plugin


__copyright__ = "Copyright (C) 2014 Mark de Reijer - Released under Creative Commons - Attribution - Share Alike (CC BY-SA) terms"

import re

with open(filename, "r") as f:
	lines = f.readlines()

z = 0
changeState = 0
with open(filename, "w") as f:
	for line in lines:
		if ";LAYER:0" in line:
			f.write("G1 Z%f \n" % (startHeight))
			f.write("G92 Z0 \n")
		f.write(line)
		
