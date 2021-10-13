import pygame
from gameObject import GameObject

class Player(GameObject):
    # Inherits from GameObject
    # Player needs an attribute for speed
    # Player needs functions for movement and collision
    # Game object shouldnt necessarily move
    def __init__(self, x,y,width,height,image_path,speed):
        # if you want the player to be the same size and same image can ommit those params
        # Call the GameObject initializer using super()
        super().__init__(x,y,width,height,image_path)
        # specific to Player class, speed
        self.speed = speed
    
    def move(self, direction, boundary):
        # move the player up or down, not left and right
        # will determine the direction key in Event Handler
        # up arrow negative, down arrow positive
        
        # before moving, check if you have reached the max or minimum height
        # want to stop players movement when y = height-playerheight
        if (self.y >= boundary-self.height and direction > 0) or (self.y == 0 and direction < 0):
            # only return if trying to move off the screen
            return
        self.y += (direction * self.speed)
    