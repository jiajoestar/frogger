from pygame import *

init()

width = 500
height = 600
screen = display.set_mode((width, height))
background = image.load("background.png")
background = transform.scale(background, (500,600))

score = 0

playerImage = image.load("kirby.png")
playerImage = transform.scale(playerImage, (80,40))
obstacle1 = image.load("car.png")
obstacle1 = transform.scale(obstacle1, (40,20))
obstacle2 = image.load("car2.png")
obstacle2 = transform.scale(obstacle2, (40,20))
obstacle3 = image.load("log.png")
obstacle3 = transform.scale(obstacle3, (60,20))
obstacle4 = image.load("turtles.png")
obstacle4 = transform.scale(obstacle4, (40,40))

# creating obstacles
def createCars():
	cars = []
	x = 0
	while len(cars) < 3:
		cars.append(Rect(x,480,20,10))
		cars.append(Rect(x,400,20,10))
		x += 150
		
	return cars
	

# drawing cars
def drawCars(cars, screen):
	for i in cars:
		screen.blit(obstacle1, i)
		screen.blit(obstacle2, i)
		

# creating turtles
def createTurtles():
	turtles = []
	x = 0
	
	while len(turtles) < 3: 
		turtles.append(Rect(x,150,40,40))
		x += 200
		
	return turtles 

# drawing turtles
def drawTurtles(turtles, screen):
	for i in turtles:
		screen.blit(obstacle4, i)


# creating logs
def createLogs():
	logs = []
	x = 0
	
	while len(logs) < 4:
		logs.append(Rect(x,200,60,20))
		logs.append(Rect(x,250,60,20))
		x += 250
		
	return logs
	
# drawing logs
def drawLogs(logs, screen):
	for i in logs:
		screen.blit(obstacle3, i)

# set up player
px = 20
py = 20

# setting up obstacles
cars = createCars()
turtles = createTurtles()
logs = createLogs()
dx = 2
player = Rect(220,500,80,40)

# game loop
gameOver = False
while gameOver == False:
	for e in event.get():
		if e.type == QUIT:
			gameOver = True
		if e.type == KEYDOWN:
			if e.key == K_LEFT:
				player.move_ip(-px,0)
			if e.key == K_RIGHT:
				player.move_ip(px,0)
			if e.key == K_SPACE:
				player.move_ip(0,-py)
				
	# draw background
	screen.blit(background, (0,0))
	
	for i in cars:
		i.move_ip(dx,0)
		screen.blit(obstacle1,i)
		
		
	for i in cars:
		if i.x >= width:
			cars.remove(i)
			cars.append(Rect(0,480,20,10))
			cars.append(Rect(0,400,20,10))	
			
			
	for i in cars:
		if player.colliderect(i):
			player.update(220,500,80,40)
	
	for j in turtles:
		j.move_ip(-dx,0)
		screen.blit(obstacle4,j)
		
	for j in turtles:
		if j.x <= 0:
			turtles.remove(j)
			turtles.append(Rect(width,150,40,40))
	
	for j in turtles:
		if player.colliderect(j):
			player.update(220,500,60,40)
	
	for k in logs:
		k.move_ip(dx,0)
		screen.blit(obstacle3,k)
		
	for k in logs:
		if k.x >= width:
			logs.remove(k)
			logs.append(Rect(0,200,60,20))
			logs.append(Rect(0,250,60,20))
			
	for k in logs:
		if player.colliderect(k):
			player.update(220,500,60,40)
	
			
		
	screen.blit(playerImage, player)
	
	# move player
	display.flip()
	time.delay(10)
	
 

