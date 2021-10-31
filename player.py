from animal import Animal 
import pygame 
import constants 

class Player(Animal):

  def __init__(self,animalNme):
    super().__init__(animalNme)

    #player data
    self.health = 30
    self.score = 0
    self.is_colliding_enemy = False
    self.is_colliding_star = False

    #star collisiond debounce timer
    self.starDebounceTimer = 0
    self.starDebounceInterval = 100

    #rotation variables
    self.rotationSpeed = 12
    self.rotationTimer = 0
    self.rotationInterval = 25

  def update(self):
    super().update()

    if self.is_colliding_star:
      self.starDebounceTimer += self.elapsed_ticks 
      if self.starDebounceTimer > self.starDebounceInterval:
        self.is_colliding_star = False
        self.starDebounceTimer = 0

    if self.is_colliding_enemy:
      rotate = pygame.transform.rotate 
      self.image = rotate(self.originalImage,self.rotationSpeed)

      self.rotationTimer += self.elapsed_ticks 
      if self.rotationTimer > self.rotationInterval:
        self.rotationSpeed += 12
        self.rotationTimer = 0
    
    if self.rotationSpeed > 360:
      self.is_colliding_enemy = False
      self.rotationSpeed = 12
      self.image = self.originalImage
     
  
  def fallOffScreen(self):
    if not self.isMoving:
      self.isMoving = True 
      self.new_pos = (self.old_pos[0],constants.SCREEN_SIZE[1] + 50)
    
  def followMouse(self,mousePos):
     if not self.isMoving:
      self.isMoving = True
      self.new_pos = mousePos

  def moveLeft(self):
    if not self.isMoving:
      self.isMoving = True
      print("Moving left...")
      self.new_pos = self.rect.move(-self.speed,0).center

  def moveRight(self):
    if not self.isMoving:
      self.isMoving = True
      print("Moving right...")
      self.new_pos = self.rect.move(self.speed,0).center  
  
  def moveUp(self):
    if not self.isMoving:
      self.isMoving = True
      print("Moving up...")
      self.new_pos = self.rect.move(0,-self.speed).center
  
  def moveDown(self):
    if not self.isMoving:
      self.isMoving = True
      print("Moving down...")
      self.new_pos = self.rect.move(0,self.speed).center
    