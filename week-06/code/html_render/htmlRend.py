#htmlRend.py
import sys

class Element(object):

	tagName = 'html'
	indentation = '    '

	def __init__(self, c=None):
		self.clist = c

	def append(self, e):
		self.clist = e

	def render(self, file_out, ind=''):
		fo = '<'
		fc = '>'		
		file_out.write(ind)
		file_out.write(fo + self.tagName + fc)
		file_out.write(self.clist)
		file_out.write(fo + '/' + self.tagName + fc)


if __name__ == "__main__":

	f = open('htmlTest.html', 'w')

	page = Element()

	page.append("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")

	page.render(f)
	
	print f.read()
	f.reset()

