#htmlRend.py
import sys

class Element(object):

	tagName = 'html'
	indent = '    '

	def __init__(self, content=None):
		self.clist = [content]

	def append(self, e):
		self.clist.append(e)

	def render(self, file_out, ind='  '):
		fo = '<'
		fc = '>'
		for i in self.clist:
			
			file_out.write(ind)
			file_out.write(fo + self.tagName + fc)
			file_out.write(self.clist)
			file_out.write(fo + '/' + self.tagName + fc)
			

class Body(Element):
	def __init__(self, content=None):
		self.tagName = "Body"
	print "Body"

class Paragraph(Element):
	print "Paragraph"

class Html(Element):
	print "Html"

class Head(Element):
	print "Element"


if __name__ == "__main__":

	import sys, cStringIO
	
	f = cStringIO.StringIO()


	## Calling Code Step 2
	page = Html()

	body = Body()

	#body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

	page.append(body)

	## End

	page.render(f)
	f.reset()	
	print f.read()


