s = raw_input()
c = ""
o = ""
for l in s:
	if l != c:
		o += l
	c = l
print o