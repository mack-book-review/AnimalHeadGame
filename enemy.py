from animal import Animal 
import constants
import random

class Enemy(Animal):

  def __init__(self,animalName,enemySpeed):
    super().__init__(animalName)
    self.setRandomPosition()
    self.speed = enemySpeed
    self.moveInterval = random.randint(200,500)

  def setRandomPosition(self):
    randX,randY = self.getRandomPosition()
    self.setPosition(randX,randY)

  def getRandomPosition(self):
    hBound,vBound = constants.SCREEN_SIZE
    randX = random.randrange(10,hBound-10)
    randY = random.randrange(10,vBound-10)
    return randX,randY

  def checkBounds(self):
    if self.isMoving:
      hBound,vBound = constants.SCREEN_SIZE

      if self.rect.left < 0 + self.rect.width:
        self.isMoving = False
        self.new_pos = self.getRandomPosition()
        self.moveTimer = 0
        self.old_pos = self.rect.center
        self.isMoving = True
    
      if self.rect.right > hBound - self.rect.width:
        self.isMoving = False
        self.new_pos = self.getRandomPosition()
        self.moveTimer = 0
        self.old_pos = self.rect.center
        self.isMoving = True

      if self.rect.top < 0 + self.rect.height:
        self.isMoving = False
        self.new_pos = self.getRandomPosition()
        self.moveTimer = 0
        self.old_pos = self.rect.center
        self.isMoving = True


      if self.rect.bottom > vBound - self.rect.height:
        self.isMoving = False
        self.new_pos = self.getRandomPosition()
        self.moveTimer = 0
        self.old_pos = self.rect.center
        self.isMoving = True



  def moveRandomly(self):
    if not self.isMoving:
      self.isMoving = True
      randMoveX = random.randrange(-self.speed,self.speed)
      randMoveY = random.randrange(-self.speed,self.speed)

      self.new_pos = self.rect.move(randMoveX,randMoveY).center
    
  def update(self):
    self.checkBounds()
    self.moveRandomly()
    super().update()