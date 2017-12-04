
# py-paper.py
# rotates a folder of background images
# images should be names in format 1BACKGROUND.jpg - 45BACKGROUND.jpg


import sys
import time
from appscript import app, mactypes

if len(sys.argv) == 3:
	# if values are supplied by user correctly then sub
	cyclewindow = int(sys.argv[1]) * 60
	upperceiling = int(sys.argv[2]) * 60
else:
	# if not then default to change every two minutes for 1 hour
	cyclewindow = 120
	upperceiling = 3600

# infinite loop

endtime = time.time() + upperceiling
while (1):
	if time.time() >= endtime:
		break
	durationminute = float(cyclewindow / 60)
	cycleminute = float(upperceiling / 60)
	print ("mypypaper is now changing the background every %i minutes for %i minutes." % (durationminute, cycleminute))
	# 1 - 45 pictures
	for x in range(1, 46):
		# concatenate path to images 
		mypath = '~/mypypaper/img/' + str(x) +'BACKGROUND.jpg'
		# update background image
		app('Finder').desktop_picture.set(mactypes.File(mypath))
		# stall for two minutes. value is in seconds / 120
		time.sleep(cyclewindow)
		if time.time() >= endtime:
			break

# done(
print ("mypypaper is now complete.")