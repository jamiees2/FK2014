import re
patv4 = re.compile("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
patv6 = re.compile("^[abcdef0-9]{4}:[abcdef0-9]{4}:[abcdef0-9]{4}:[abcdef0-9]{4}:[abcdef0-9]{4}:[abcdef0-9]{4}:[abcdef0-9]{4}:[abcdef0-9]{4}")
s = raw_input()
m = patv4.match(s)
m2 = patv6.match(s)
if m:
	for i in xrange(4):
		if m.group(i+1):
			p = int(m.group(i+1))
			if p < 0 or p > 255 or str(p) != m.group(i+1):
				print "Error"
				break
	else:
		print "IPv4"
elif m2:
	print "IPv6"
else:
	print "Error"
