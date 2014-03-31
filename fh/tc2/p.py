from math import sqrt
def edist(p1,p2):
	p1x, p1y = p1
	p2x, p2y = p2
	return sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
N = input() - 1
p1 = [float(_) for _ in raw_input().split()]
s = 0
for i in xrange(N):
	p2 = [float(_) for _ in raw_input().split()]
	s += edist(p1,p2)
	p1 = p2
print s