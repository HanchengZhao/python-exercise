# -*- coding: utf-8 -*-

""" count the number of words in a book
"""

import string

def process_file(filename):
	hist = dict()	
	fp = open(filename)
	for line in fp:
		process_line (line, hist)
	return hist

def process_line(line, hist):
	line = line.replace('-', ' ')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)#remove punctuation
		word = word.lower()

		hist[word] = hist.get(word, 0) + 1

hist = process_file('emma.txt')

def total_word(hist):
	return sum(hist.values())

def different_words(hist):
	return len(hist)

if __name__ == '__main__':
	hist = process_file('emma.txt')

	print 'Total number of words: ', total_word(hist)
	print 'Number of different_words', different_words(hist)