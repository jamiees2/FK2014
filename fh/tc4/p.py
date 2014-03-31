N = input()
popcorns = sorted([[int(_) for _ in raw_input().split()] for x in xrange(N)],key=lambda k: k[0])
mc = 0
mp = 0
lastp = -1
for pop in popcorns:
	c = 0
	if pop[0] == lastp:
		continue
	for pop2 in popcorns:
		if pop2[0] <= pop[0] and pop2[0] + pop2[1] -1 >= pop[0]:
			c += 1
		elif pop2[0] > pop[0]:
			break
	lastp = pop[0]
	if c > mc :
		mp = pop[0]
		mc = c
print mp, mc