import turtle


class Draw():
	startColor = "red"
	goalColor = "green"
	pointColor = "black"
	exploreColor = 'purple'
	pathColor = "red"
	
	minX, minY = 8,8
	maxX, maxY = 25,25
	
	def __init__(self, start):
		'''
		Initializes the drawing class: 
		Creates a turtle
		Sets up the screen for drawing
		Puts turtle on start and draws a dot to represent it 
		'''
		self.t = turtle.Turtle()
		self.t.getscreen().setworldcoordinates(Draw.minX, Draw.minY, Draw.maxX, Draw.maxY)
		self.t.speed(0)
		self.t.hideturtle()
		self.t.getscreen().tracer(300)
		self.t.penup()
		self.t.goto(start)
		self.t.dot(Draw.startColor)
		
	def drawGoals(self, goals):
		'''
		Begin state: an initialized Draw
		Saves X,Y pos of turtle
		Marks goals (given in list of tuples)
		Returns turtle to intial point 
		'''
		startX, startY =  self.t.xcor(), self.t.ycor() 
		self.t.penup()
		for goal in goals:
			self.t.goto(goal)
			self.t.dot(Draw.goalColor)
		self.t.goto(startX, startY)
		
	def visitPoint(self, point):
		self.t.penup()
		self.t.goto(point)
		self.t.dot(Draw.pointColor)
		
	def explorePoint(self, point):
		startPoint = self.t.xcor(), self.t.ycor()
		self.t.pendown()
		self.t.goto(point)
		self.t.dot(Draw.exploreColor)
		self.t.goto(startPoint)
		
	def reset(self):
		self.t.reset()
		
	def drawPath(self, path):
		self.t.width(3)
		self.t.color(Draw.pathColor)
		self.t.penup()
		self.t.goto(path[0])
		self.t.pendown()
		for node in path:
			self.t.goto(node)
			self.t.dot(Draw.pathColor)
		
		