import math
import pprint
class pointInfo:
	x = 0
	y = 0
	steps = 0
	def __hash__(self):
		return hash((self.x, self.y))
	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)
	def toString(self):
		return str(self.x) + "," + str(self.y) + "," + str(self.steps)
		

def loadWires(fileName):
	with open(fileName) as inf:
		wires = inf.read()
		wires = wires.split("\n")
	return wires		

a = loadWires("numbers.txt")

directions1 = a[0]
directions2 = a[1]

#def createGrid(rows, cols):
	#grid =[['X' for i in range(cols)] for j in range(rows)]
	#return grid
def drawWire(directions):
	directions = directions.split(",")
	wire = set()
	x = 0
	y = 0
	steps = 0
	for string in directions:
		dir = string[0]
		distance = int(string[1:])
		for i in range(0, distance):
			if dir == 'R':
				x += 1
			if dir == 'L':
				x -= 1
			if dir == 'U':
				y += 1
			if dir == 'D':
				y -= 1
			steps += 1
			point = pointInfo()
			point.x = x
			point.y = y
			point.steps = steps
			wire.add(point)		
	return wire					

wire1 = drawWire(directions1)
wire2 = drawWire(directions2)

allIntersections = wire1.intersection(wire2)
temp = []
coordinates = []
for point in allIntersections:
	print(pointInfo.toString(point))
	coordinates.append(str(point.x)+","+str(point.y))

for k in wire2:
	testval = str(k.x)+","+str(k.y)
	if testval in coordinates:
		temp.append(k)
		print(pointInfo.toString(k))

allSteps = []
for i in allIntersections:
	for k in temp:
		if (i.x == k.x and i.y == k.y):
			allSteps.append(i.steps + k.steps)	
print(min(allSteps))
