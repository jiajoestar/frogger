from pygame import *

init()

width = 1200
height = 1200
screen = display.set_mode((width, height))

gameOver = False
score = 0

playerImage = image.load("kirby.png")
playerImage = transform.scale(playerImage, (40,40))
obstacle1 = image.load("car.png")
obstacle1 = transform.scale(obstacle1, (40,20))
obstacle2 = image.load("log.png")
obstacle2 = transform.scale(obstacle2, (60,10))
obstacle3 = image.load("turtles.png")
obstacle3 = transform.scale(obstacle3, (40,40))

# creating obstacles
def createCars():
	cars = []
	y = 50
	num_rows = 5
	num_cars_rows = 5
	
	while y <= 50 * num_rows: #50 is the height
		x = 50 #where car is placed inside the row
		while x <= 50 * num_cars_rows:
			cars.append(Rect(x,y,50,50))
			x = x + 50
		y = y + 50
		
	return cars

# drawing cars
def drawCars(cars, screen):
	for i in cars:
		screen.blit(obstacle1, i)

# moving cars
def moveCars(cars, dx):
	for i in cars:
		if i.right > width or i.left < 0:
			dx = dx * -1
			for car in cars:
				car.move_ip(0,50)
			break
				
	for i in car:
		i.move_ip(dx,0)
	
	return dx

# set up player
px = 0
player = Rect(600,600,100,100)

# setting up obstacles
cars = createCars()
dx = 1
framecount = 0

# game loop
while not gameOver:
	for e in event.get():
		if e.type == QUIT:
			gameOver = True
		elif e.type == KEYDOWN:
			if e.key == K_LEFT:
				px = -3
			if e.key == K_RIGHT:
				px = 3
		elif e.type == KEYUP:
			if e.key == K_LEFT or e.key == K_RIGHT:
				px = 0
				
	if framecount >= 100:
		dx = moveCars(cars, dx)
		framecount = 0
	framecount = framecount + 1
	# move player
	if player.left+px < 0 or player.right+px > width:
		px = 0
		player.move_ip(px,0)
 
#



