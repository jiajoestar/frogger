from pygame import *

init()

width = 1200
height = 1200
screen = display.set_mode((width, height))

gameOver = False
score = 0

playerImage = image.load("kirby.png")
playerImage = transform.scale(playerImage, (40,40))
obstacle1 = image.load()
obstacle2 = image.load()

# set up player
px = 0
player = Rect(600,600,100,100)

# setting up obstacles

while not gameOver:
  for e in event.get():
    if e.type == QUIT:
      gameOver = True
    elif e.type == KEYDOWN:
      if e.key == K_LEFT:
        px = -3
      if e.key == K_RIGHT:
        px = 3
      if e.key == K_


