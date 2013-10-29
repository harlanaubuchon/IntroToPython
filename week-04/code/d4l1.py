##d4l1.py

d = {}
lkey = ['name', 'city', 'cake']
lvalue = ['Chris', 'Seattle', 'Chocolate']

def dictMaker():
	##Excercise 1
	d = dict(zip(lkey, lvalue))
	print d
	del d['cake']
	print 'removed cake from dictionary'
	print d
	d['fruit']='Mango'
	print d
	print d.keys()
	print d.values()
	if 'cake' in d.keys():
		print "'cake' is in the dictionary"
	else:
		print "'cake' is not in the dictionary"
	if 'Mango' in d.values():
		print "'Mango' is in the dictionary"
	else:
		print "'Mango' is not in the dictionary"

	##Excercise 2
	f = dict([(x, hex(x)) for x in range(16)])
	print 'Dictionary of 0-15: Hex'
	print f