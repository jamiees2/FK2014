x,y = [ int(i) for i in raw_input().strip().split() ]
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
    def move_cost(self,other):
        return 0 if self.value == '.' else 1
        
def children(point,grid):
    x,y = point.point
    points = []
    
    for p in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]:
        # print "Point",p
        if not (p[0] < 0 or p[0] >= len(grid) or p[1] < 0 or p[1] >= len(grid[0])):
            points.append(p)
    links = [grid[d[0]][d[1]] for d in points]
    links = [link for link in links if link.value =="."]
    print [(link.point, link.value) for link in links]
    return links
def manhattan(point,point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])
def aStar(start, goal, grid):
    #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the starting point
    current = start
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings
        for node in children(current,grid):
            print node.point, node.value,current.move_cost(node)
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')
# def next_move(pacman,food,grid):
    #Convert all the points to instances of Node
    
# pacman_x, pacman_y = [ int(i) for i in raw_input().strip().split() ]
# food_x, food_y = [ int(i) for i in raw_input().strip().split() ]


robots = []
grid = []
for i in xrange(0, x):
    c = list(raw_input().strip())
    grid.append(c)
    for a,b in enumerate(c):
        if b == "X":
            robots.append((a,i))
# print grid,robots
print robots

#Get the path
for robot in robots:
    grid2 = []
    for x in xrange(len(grid)):
        grid2.append([])
        print grid[x]
        for y in xrange(len(grid[x])):
            grid2[x].append(Node(grid[x][y],(x,y)))
    print grid2[1][5].value == "."
    try:
    # print robot, grid[robot[0]][robot[1]].value
        path = aStar(grid2[robot[0]][robot[1]],grid2[0][0],grid2)
        print [p.point for p in path]
        print "Death to humans"
        break
    except ValueError:
        print "stuff"
        pass
else:
    print "We are safe"
#Output the path
# print path
# print len(path) - 1
# for node in path:
#     x, y = node.point
#     print x, y
# next_move((pacman_x, pacman_y),(0,0), grid)