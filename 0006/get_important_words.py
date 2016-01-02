# -*- coding: utf - 8 -*-

import re 
import os
import string

# Get all files in the designated path(including subpath)
def get_files(path):
	filepath = os.listdir(path)
	files = []
	for fp in filepath:
		fppath = path + '/' + fp
		if (os.path.isfile(fppath)):
			files.append(fppath)
		elif(os.path.isdir(fppath)):
			files += get_files(fppath)
	return files

#Get the most popular words
def get_popular_words(files):
	worddict = dict()
	for filename in files:
		f = open(filename, 'rb')
		s = f.read()
		for line in s:
			line = line.replace('-', ' ')

			for word in line.split():
				word = word.strip(string.punctuation + string.whitespace)#remove punctuation
				word = word.lower()
				worddict[word] = worddict[word] + 1 if word in worddict else 1
		f.close
	wordsort = sorted(worddict.items(), key = lambda e:e[1], reverse = True)
	return wordsort

if __name__ == '__main__':
	files = get_files('.')
	print files
	wordsort = get_popular_words(files)
    #in case there are mutiple maximums
	maxnum = 1
	for i in range(len(wordsort) - 1):
		if wordsort[i][1] == wordsort[i + 1][i]:
			maxnum += 1
		else:
			break
	for i in range(maxnum):
		print wordsort[i]
