# - * - coding: utf - 8 - * -

import glob
import os

#get all the files in the designated path
def get_files(path):
	return glob.glob(path + r'/*')

#count lines in the designated directory, including blank lines and note lines
def count_lines(files):
	line, blank, note = 0, 0, 0
	for filename in files:
		f = open(filename, 'rb')
		for l in f:
			l = l.strip()
			line += 1
			if l == '':
				blank += 1
			elif l[0] == '#' or l[0] == '/':
				note += 1
		f.close
	return (line, blank, note)

if __name__ == '__main__':
	files = get_files('.')
	print files
	lines = count_lines(files)
	print "Line(s): %d, blank line(s): %d, note line(s): %d" %(lines[0], lines[1], lines[2])