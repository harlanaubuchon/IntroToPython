##d4c1.py
import os

def dothis():
    try:
    	os.path.exists('missing.txt')
        f = open('missing.txt')
        process(f)
    except IOError:
    	print "couldn't open missing.txt"
    finally:
    	print "cleanup"

def dothis2():
    try:
    	os.path.exists('missing.txt')
        f = open('missing.txt')
        process(f)
    except IOError as error:
    	print error
    	##print error.extra_info = "couldn't open missing.txt"
    	raise
    finally:
    	print "cleanup"