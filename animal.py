import pygame 
import os
from functions import load_image
import constants
import random 

class Animal(pygame.sprite.Sprite):

  def __init__(self,animalName):
    super().__init__()
    fullName = os.path.join("assets",animalName + ".png")

    #load the image
    self.image = load_image(fullName,constants.BLACK)

    #scale down the image
    self.image = pygame.transform.scale(self.image,(50,50))
    self.originalImage = self.image 
    
    self.rect = self.image.get_rect()
    self.x = self.rect.x 
    self.y = self.rect.y  

    #initialize position data
    self.old_pos = None
    self.new_pos = None

    #initialize speed data
    self.speed = 30

    self.prev_ticks = 0 
    self.current_ticks = 0
    self.elapsed_ticks = 0
    self.isMoving = False 
    self.moveTimer = 0
    self.moveInterval = 200
  
  def setPosition(self,x,y):
    self.rect.center = x,y
    self.old_pos = self.rect.center
  
 
  
  
  def lerp(self,old_pos,new_pos,percent):
    if old_pos and new_pos:
      dist_x = (new_pos[0] - old_pos[0])*percent
      dist_y = (new_pos[1] - old_pos[1])*percent
      self.rect.centerx = old_pos[0] + dist_x
      self.rect.centery = old_pos[1] + dist_y

  def update(self):
   
    self.current_ticks = pygame.time.get_ticks()
    self.elapsed_ticks = self.current_ticks - self.prev_ticks
    #print("Elapsed ticks: " + str(self.elapsed_ticks))

    if self.isMoving:
      self.moveTimer += self.elapsed_ticks 
      percent = self.moveTimer/self.moveInterval
      self.lerp(self.old_pos,self.new_pos,percent)

      if self.moveTimer >= self.moveInterval:
        self.moveTimer = 0 
        self.isMoving = False
        self.old_pos = self.new_pos
        self.new_pos = None


     
    
    
    self.prev_ticks = self.current_ticks
   

    