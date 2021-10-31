import pygame 
import sys,os
import constants
from animal import Animal 
from player import Player 
from enemy import Enemy 
from game import Game


def main():
  game = Game() 
  game.runGame() 

if __name__ == "__main__":
  main()