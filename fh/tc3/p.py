# | | |-| | |
# |-| | |-| |
# | | |-| |-|
# | |-| |-| |
# | |-| | |-|
N, K = [int(_) for _ in raw_input().split()]
lines = []
for _ in xrange(K):
	lines.append([c for c in raw_input()])
R = len(lines[0]) - 1
def trace(table,s):
	# s *= 2
	i = 0
	while i < K:
		if s < R and lines[i][s+1] == "-":
			s += 2
		elif s > 0 and lines[i][s-1] == "-":
			s -= 2
		i += 1
	return s/2

students = map(chr, range(65, 91))
s = [""] * N
for i in xrange(N):
	p = trace(lines,i * 2)
	s[p] = students[i]
print "".join(s)


