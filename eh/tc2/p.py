import re

s = raw_input()
r = "^"
for c in s:
	if c == "*":
		r += ".*"
	else:
		r += re.escape(c)
r += "$"
regex = re.compile(r)

N = input()
for t in xrange(N):
	if regex.match(raw_input()):
		print "Passar"
	else:
		print "Passar ekki"