import pygame 
import os
from functions import load_image
import constants
import random 

class Star(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    fullName = os.path.join("assets","star.png")

    #load the image
    self.image = pygame.image.load(fullName)
    
    #scale down the image
    self.image = pygame.transform.scale(self.image,(50,50))
    self.originalImage = self.image 
    
    #transform variables
    self.rect = self.image.get_rect()
    self.x = self.rect.x 
    self.y = self.rect.y  

    #set starting position randomly
    self.setRandomPosition()

    #timer variables
    self.prev_ticks = 0 
    self.current_ticks = 0
    self.elapsed_ticks = 0


    self.isExpanding = False
    self.animationTimer = 0
    self.animationInterval = 200
  
  def setPosition(self,x,y):
    self.rect.center = x,y
    self.old_pos = self.rect.center
  
  def setRandomPosition(self):
    randX,randY = self.getRandomPosition()
    self.setPosition(randX,randY)
  
  def getRandomPosition(self):
    hBound,vBound = constants.SCREEN_SIZE
    randX = random.randrange(10,hBound-50)
    randY = random.randrange(10,vBound-50)
    return randX,randY
  
 

  def update(self):
   
    self.current_ticks = pygame.time.get_ticks()
    self.elapsed_ticks = self.current_ticks - self.prev_ticks
    #print("Elapsed ticks: " + str(self.elapsed_ticks))

     
    self.animationTimer += self.current_ticks

    if self.animationTimer > self.animationInterval:
      self.isExpanding = not self.isExpanding
      self.animationTimer = 0

    if self.isExpanding:
      self.rect.inflate_ip(1,1)
    else:
      self.rect.inflate_ip(-1,-1)

    
    self.prev_ticks = self.current_ticks