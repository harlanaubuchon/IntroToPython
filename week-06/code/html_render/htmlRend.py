#htmlRend.py

class Element(something):
	fO = '<'
	fC = '>'
	tagName = ''
	indentation = ''

    def __init__(self, c):
    	self.content = c

	def append(self, s):
		self.content += s

	def render(self, file_out, ind=''):
		self.

