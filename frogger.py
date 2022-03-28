from pygame import *

init()

width = 500
height = 800
screen = display.set_mode((width, height))
background = (0,0,0)
river = (30,144,255)

score = 0

playerImage = image.load("kirby.png")
playerImage = transform.scale(playerImage, (80,40))
obstacle1 = image.load("car.png")
obstacle1 = transform.scale(obstacle1, (40,20))
obstacle2 = image.load("log.png")
obstacle2 = transform.scale(obstacle2, (60,10))
obstacle3 = image.load("turtles.png")
obstacle3 = transform.scale(obstacle3, (40,40))

# creating obstacles
def createCars():
	cars = []
	x = 0
	while len(cars) < 3:
		cars.append(Rect(x,400,20,10))
		x += 150
		
	return cars
	
#def createCars2():
#	cars2 = []
#	x = 0
#	while len(cars2) < 3:
#		cars2.append(Rect(x,300,20,10))
#		x += 150
#	return cars2

# drawing cars
def drawCars(cars, screen):
	for i in cars:
		screen.blit(obstacle1, i)
		
#def drawCars2(cars2, screen):
#	for i in cars2:
#		screen.blit(obstacle1, i)

'''
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
	'''
# creating turtles
def createTurtles():
	turtles = []
	y = 50
	num_rows = 2
	num_turtles_rows = 3
	
	while y <= 50 * num_rows: 
		x = 30 
		while x <= 30 * num_turtles_rows:
			turtles.append(Rect(x,y,40,40))
			x = x + 400
		
	return turtles 

# drawing turtles
def drawTurtles(turtles, screen):
	for i in turtles:
		screen.blit(obstacle3, i)

# moving turtles
#def moveTurtles(turtles, dx):
#	for i in turtles:
#		if i.right > width or i.left < 0:
#			dx = dx * -1
#			for turtle in turtles:
#				turtles.move_ip(0,50)
#			break
				
#	for i in turtle:
#		i.move_ip(dx,0)
	
#	return dx

# creating logs
def createLogs():
	logs = []
	y = 20
	num_rows = 2
	num_logs_rows = 2
	
	while y <= 20 * num_rows: 
		x = 10 
		while x <= 10 * num_logs_rows:
			logs.append(Rect(x,y,60,10))
			x = x + 400
		
	return logs
	
# drawing logs
def drawLogs(logs, screen):
	for i in logs:
		screen.blit(obstacle2, i)

# moving logs
#def moveLogs(logs, dx):
#	for i in logs:
#		if i.right > width or i.left < 0:
#			dx = dx * -1
#			for log in logs:
#				log.move_ip(0,50)
#			break
#				
#	for i in log:
#		i.move_ip(dx,0)
#	
#	return dx

# set up player
px = 20
py = 20
# setting up obstacles
cars = createCars()
#cars2 = createCars2()
turtles = createTurtles()
logs = createLogs()
dx = 2
#framecount = 0
player = Rect(250,600,80,40)
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
	screen.fill(background)
	#draw.rect(screen, river, (0,250,500,500))
	
	for i in cars:
		i.move_ip(dx,0)
		screen.blit(obstacle1,i)
		
		
	for i in cars:
		if i.x >= width:
			cars.remove(i)
			cars.append(Rect(0,400,20,10))
			
	for i in cars:
		if player.colliderect(i):
			player.update(250,600,80,40)
			
#	for i in cars2:
#		i.move_ip(-dx,0)
#		screen.blit(obstacle1,i)
#		
#	for i in cars2:
#		if i.x <= width:
#			cars2.remove(i)
#			cars2.append(Rect(0,300,20,10))		
#	
#			
#	for i in turtles:
#		i.move_ip(dx,0)
#		screen.blit(obstacle3,i)
#	
#	for i in turtles:
#		if i.x >= width:
#			turtles.remove(i)
#			turtles.append(Rect(0,100,40,20))
#			
#	
#	for i in logs:
#		i.move_ip(dx,0)
#		screen.blit(obstacle2,i)
#		
#		
	screen.blit(playerImage, player)
	
	
		
	#drawCars = (cars, screen)
	
	
	
				
#	if framecount >= 100:
#		dx = moveCars(cars, dx)
#		framecount = 0
#	framecount = framecount + 1
	# move player
	display.flip()
	time.delay(10)
	
 
#



