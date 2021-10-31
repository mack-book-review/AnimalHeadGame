import pygame 
import os
from functions import load_image
import constants
import random 
import math 

class HUD(object):

  def __init__(self):

    #initiali font module
    pygame.font.init()
    self.hud_font = pygame.font.SysFont('Comic Sans MS',30)

    #load the image
    print("Initializing HUD...")
    self.emptyHeart = load_image("assets/hud_heartEmpty.png",constants.BLACK)
    self.halfHeart = load_image("assets/hud_heartHalf.png",constants.BLACK)
    self.fullHeart = load_image("assets/hud_heartFull.png",constants.BLACK)

    #scale down the image
    self.emptyHeart = pygame.transform.scale(self.emptyHeart,(50,50))
    self.halfHeart = pygame.transform.scale(self.halfHeart,(50,50))
    self.fullHeart = pygame.transform.scale(self.fullHeart,(50,50))

    self.rect = self.emptyHeart.get_rect()
    self.width = self.rect.width

    self.startX = 20
    self.startY = 20

    self.originalPlayerHealth = 20
    self.currentPlayerHealth = 20
    self.previousHealth = self.currentPlayerHealth

  def update(self,screen,playerHealth,playerScore):
    self.draw(screen) 
    textX,textY = constants.SCREEN_SIZE
    textX -= 100
    textY -= 50
    hud_text = self.hud_font.render(f'Score: {playerScore}', False, constants.BLACK)
    screen.blit(hud_text,(textX,textY))

    if playerHealth != self.previousHealth:
      self.currentPlayerHealth = playerHealth
      self.previousHealth = self.currentPlayerHealth
    
  
  
  def totalHearts(self):
    return self.originalPlayerHealth//2 

  def totalFull(self):
    return self.currentPlayerHealth//2

  def remainingHearts(self):
    return self.totalHearts() - self.totalFull() 

  def draw(self,screen):
    x = self.startX
    y = self.startY
    if self.currentPlayerHealth >= 25:
      for i in range(3):
        x = i*self.width + self.startX 
        self.drawHeart(screen,2,x,y)
    elif self.currentPlayerHealth >= 20: 
      for i in range(3):
        x = i*self.width + self.startX
        if i == 2:
          self.drawHeart(screen,1,x,y) 
        else:
          self.drawHeart(screen,2,x,y)
    elif self.currentPlayerHealth >= 15:
      for i in range(3):
        x = i*self.width + self.startX 
        if i == 2:
          self.drawHeart(screen,0,x,y) 
        elif i == 1:
          self.drawHeart(screen,1,x,y) 
        else:
          self.drawHeart(screen,2,x,y)    
    elif self.currentPlayerHealth >= 10:
      for i in range(3):
        x = i*self.width + self.startX
        if i >= 1:
          self.drawHeart(screen,0,x,y) 
        else:
          self.drawHeart(screen,2,x,y) 
    elif self.currentPlayerHealth >= 5:
      for i in range(3):
        x = i*self.width + self.startX
        if i >= 1:
          self.drawHeart(screen,0,x,y)  
        else:
          self.drawHeart(screen,1,x,y)  
    else: 
      for i in range(3):
        x = i*self.width + self.startX
        self.drawHeart(screen,0,x,y)  



  def drawHeart(self,screen,heartType,x,y):
    #drawing heart
    if heartType == 0: #emptyHeart
      screen.blit(self.emptyHeart,(x,y)) 
    elif heartType == 1: #halfHeart
      screen.blit(self.halfHeart,(x,y)) 
    elif heartType == 2: #fullHeart 
      screen.blit(self.fullHeart,(x,y)) 


      