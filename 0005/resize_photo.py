# -*- coding: utf-8 -*-
from PIL import Image

def resize_pic(path, width = 640, height = 1136):
	im = Image.open(path)
	w,h = im.size
	changew = float(w) / width
	changeh = float(h) / height

	if w > width or h > height:
		change = changew if changew >changeh else changeh
		print (change)
		im.resize((int(w / change),int (h / change))).save('result.jpg')
	else :
		print ("The picture' pixels does not exceed iPhone5's resolution")

if __name__ == '__main__':
	resize_pic('image.png')