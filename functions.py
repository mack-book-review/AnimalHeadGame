import pygame
import os 

def load_image(name,colorkey=None):
  try:
    image = pygame.image.load(name)
    image = image.convert()
    if colorkey is not None and colorkey == -1:
      colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey)
    return image
  except RuntimeError:
    print(f"Cannot load image {name}")
  



  