import string
import md5

for i in xrange(0,2000):
	m = md5.new()
	m.update('dfksdfkasdjfa' + str(i))
	print str(m.hexdigest()) + ",program" + str(i) + "," + str(i) + "source" 
	
