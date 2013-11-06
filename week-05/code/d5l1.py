## d5l1.py
import codecs
import os

lineList = []

##codecs.open(filename, mode[, encoding[, errors[, buffering]]])

unicodeFile = 'text.utf32'

def fileOpener():
	f = codecs.open(unicodeFile, encoding='utf32')
	for line in f:
		lineList.append(line)
		print repr(line)
	print '\n\n'
	for i in lineList:
		print i

def fileWriter():
	w = codecs.open('sample.txt', 'w', encoding='utf8')
	w.write('This is another test\n')
	w.close

def fileReader():
	r = codecs.open('sample.txt', encoding='utf8')
	for line in r:
		print repr(line)

