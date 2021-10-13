from gameObject import GameObject
import pygame

class Enemy(GameObject):
    def __init__(self,x,y,width,height,image_path,speed):
        super().__init__(x,y,width,height,image_path)
        self.speed = speed

    def move(self, boundary):
        # check bondaries
        # at far right change direction to left etc
        
        if self.x <= 0:
            self.speed = abs(self.speed) # absolute means +ve
        elif self.x >= boundary - self.width:
            self.speed = -self.speed

        self.x += self.speed