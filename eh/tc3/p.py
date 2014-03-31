class House:
	connections = set()
	connected = 0
	loop = False
	def __init__(self):
		self.connections = set()
		self.connected = None
		self.loop = False
	def is_connected(self,houses):
		if self.loop:
			return False
		self.loop = True
		if self.connected != None:
			return self.connected
		for a in self.connections:
			if houses[a].is_connected(houses):
				# print a,"is connected"
				# self.connected = True
				return True
		else:
			# self.connected = False
			return False
		self.loop  = False
n, m = [int(_) for _ in raw_input().split()]
connections = [[int(_) for _ in raw_input().split()] for i in xrange(m)]

houses = dict()
for i in xrange(n):
	houses[i+1] = House()
houses[1].connected = 1
for connection in connections:
	a, b = connection
	if not a in houses:
		houses[a] = House()
	if not b in houses[a].connections:
		houses[a].connections.add(b)

	if not b in houses:
		houses[b] = House()
	if not a in houses[b].connections:
		houses[b].connections.add(a)
# print houses[1].is_connected(houses)
# print houses[2].is_connected(houses)
# print houses[8].is_connected(houses)
everyone = True
for a in list(houses.keys()):
	# # print a, house
	for b, h in list(houses.iteritems()):
		h.loop = False
	# print houses[a].connections
	if not houses[a].is_connected(houses):
		everyone = False
		print a
		# pass
if everyone:
	print "Allir nettengdir"
