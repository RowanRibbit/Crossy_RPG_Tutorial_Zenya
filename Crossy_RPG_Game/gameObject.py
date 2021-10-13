import pygame

class GameObject:
    # Game objects have x and y position and image path
    def __init__(self, x, y, width, height, image_path):
        # Don't need raw image, but do need scaled up
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        # Set the x/y values and dimensions   
        self.x = x
        self.y = y
        self.width = width
        self.height = height
