import pygame, sys, os, random, constants
from functions import load_image
from animal import Animal 
from player import Player 
from enemy import Enemy
from star import Star
from hud import HUD 


class Game(object):

  def __init__(self):
    super().__init__()
    self.initialize() 

  def input(self,events):
    
    for event in events:
        if event.type == pygame.QUIT:
          sys.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if not self.isReadyStart:
            self.isReadyStart = True 
          else:
            mousePos = pygame.mouse.get_pos()
            self.player.followMouse(mousePos)
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            pass
            #self.player.moveUp()
          elif event.key == pygame.K_DOWN:
            pass
            #self.player.moveDown()
          elif event.key == pygame.K_LEFT:
            pass
            #self.player.moveLeft()
          elif event.key == pygame.K_RIGHT:
            pass
            #self.player.moveRight()


  def initialize(self):
    pygame.init()
    self.screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    self.area = self.screen.get_rect()
    startX,startY = self.area.center

    pygame.display.set_caption("Animal Head Game")
  
    #create sprite groups
    self.all_sprites = pygame.sprite.Group()
    self.enemy_list = pygame.sprite.Group()
    self.star_list = pygame.sprite.Group()

    #store gameReady and gameOver images 
    self.gameOverMessage = load_image("assets/gameOver.png")
    self.gameOverMessage.set_colorkey(constants.BLACK)

    self.gameReadyMessage = load_image("assets/gameReady.png")
    self.gameReadyMessage.set_colorkey(constants.BLACK)

    self.gameWinMessage = load_image("assets/gameWin.png")
    self.gameWinMessage.set_colorkey(constants.BLACK)


    #create background
    self.bg_image = load_image("assets/colored_castle.png")
    self.bg_image = pygame.transform.scale(self.bg_image,constants.SCREEN_SIZE)


    #create player
    self.player = Player("elephant")
    self.player.setPosition(startX,startY)
    self.all_sprites.add(self.player)

    #create initial enemies
    self.spawnEnemies(random.randint(1,3))

   
    #intialize enemy spawning timers 
    self.spawnEnemyInterval = 15000 
    self.spawnEnemyTimer = 0

    #intialize star spawning timers 
    self.starSpawningInterval = 15000 
    self.starSpawningTimer = 0

    #spawn stars 
    self.spawnStars(random.randint(1,3))

    #initialize tick variables
    self.elapsed_ticks = 0 
    self.previous_ticks = 0 
    self.current_ticks = 0

    #create HUD 
    self.hud = HUD()
    self.hud.originalPlayerHealth = self.player.health

    #game win/loss boolean flags
    self.isReadyStart = False
    self.isGameOver = False
    self.hasWon = False

  def spawnEnemies(self,numberEnemies):
    for _ in range(numberEnemies):
      e = Enemy("snake",50)
      self.all_sprites.add(e)
      self.enemy_list.add(e)
  
  def spawnStars(self,numberStars):
    for _ in range(numberStars):
      s = Star()
      self.all_sprites.add(s)
      self.star_list.add(s)
  
  def checkPlayerCollision(self):
    
    if not self.player.is_colliding_star:
      star_hit = pygame.sprite.spritecollideany(self.player,self.star_list,pygame.sprite.collide_rect_ratio(0.5))
      if star_hit:
        self.player.is_colliding_star = True
        self.player.score += 1
        star_hit.kill()
        print("New player score: " + str(self.player.score))
       

    if not self.player.is_colliding_enemy:
      player_hit = pygame.sprite.spritecollideany(self.player,self.enemy_list,pygame.sprite.collide_rect_ratio(0.5))
      if player_hit:
        self.player.is_colliding_enemy = True
        self.player.health -= 1
        print("New player health: " + str(self.player.health))
        self.player.rotationTimer = 0

  def updateEnemySpawner(self):
    self.spawnEnemyTimer += self.elapsed_ticks 
    if self.spawnEnemyTimer > self.spawnEnemyInterval:
      self.spawnEnemies(random.randint(1,3))
      self.spawnEnemyTimer = 0
  
  def updateStarSpawner(self):
    self.starSpawningTimer += self.elapsed_ticks 
    if self.starSpawningTimer > self.starSpawningInterval:
      self.spawnStars(random.randint(1,3))
      self.starSpawningTimer = 0


  def runGame(self):
    while True:

      if not self.isReadyStart:
        print("Are you ready?")
        self.screen.fill(constants.TURQUOISE)
        centerX,centerY = self.area.center
        msgRect = self.gameReadyMessage.get_rect()
        width,height = msgRect.width,msgRect.height
        finalPos = (centerX-0.5*width,centerY-height)
        self.screen.blit(self.gameReadyMessage,finalPos)
        self.input(pygame.event.get())
        pygame.display.flip()
      elif self.hasWon:
        self.screen.fill(constants.TURQUOISE)
        centerX,centerY = self.area.center
        msgRect = self.gameWinMessage.get_rect()
        width,height = msgRect.width,msgRect.height
        finalPos = (centerX-0.5*width,centerY-height)
        self.screen.blit(self.gameWinMessage,finalPos)
        pygame.display.flip()
      elif self.isGameOver:
        self.screen.fill(constants.TURQUOISE)
        centerX,centerY = self.area.center
        msgRect = self.gameOverMessage.get_rect()
        width,height = msgRect.width,msgRect.height
        finalPos = (centerX-0.5*width,centerY-height)
        self.screen.blit(self.gameOverMessage,finalPos)
        pygame.display.flip()
         
      else:
        if self.player.score > 20:
          self.hasWon = True 
          
        if self.player.rect.top > self.area.bottom:
          self.isGameOver = True

        self.current_ticks = pygame.time.get_ticks()
        self.elapsed_ticks = self.current_ticks - self.previous_ticks 

        
        self.screen.blit(self.bg_image,(0,0))

        self.all_sprites.draw(self.screen)
        self.all_sprites.update()

        if self.player.health == 0:
          self.player.fallOffScreen()
        else:
          self.input(pygame.event.get())
          self.checkPlayerCollision()
          self.updateEnemySpawner()
          self.updateStarSpawner()

        self.hud.update(self.screen,self.player.health,self.player.score)

        self.previous_ticks = self.current_ticks
        pygame.display.flip()
    print("Game finished")