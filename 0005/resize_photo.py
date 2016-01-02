# -*- coding: utf-8 -*-
from PIL import Image

def resize_pic(path, new_path, width = 640, height = 1136):
	im = Image.open(path)
	w,h = im.size