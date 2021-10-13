import pygame
from pygame.constants import K_DOWN
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:
    # Initializer - set up properties of Game
    def __init__(self):
        self.width = 800
        self.height = 800
        self.game_window = pygame.display.set_mode((self.width,self.height))
        self.bg_colour = (255,255,255)
        self.clock = pygame.time.Clock()
        self.bg = GameObject(0,0,self.width,self.height,'assets/background.png')
        self.treasure = GameObject(375,50,50,50,'assets/treasure.png')
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 5)
        self.enemies = [
            Enemy(50, 600, 50, 50, 'assets/enemy.png', 3),
            Enemy(375, 400, 50, 50, 'assets/enemy.png', 3),
            Enemy(750, 200, 50, 50, 'assets/enemy.png', 4)
        ]
        self.level = 1.0
        self.reset_map()

    def reset_map(self):
        # if you hit the treasure you need to reset all and increase level
        # if you hit enemy reset game and level
        
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 5)
        speed = 2 + (self.level * 2)
        
        if self.level >= 4.0:
            self.enemies = [
            Enemy(50, 600, 50, 50, 'assets/enemy.png', speed),
            Enemy(375, 400, 50, 50, 'assets/enemy.png', speed),
            Enemy(750, 200, 50, 50, 'assets/enemy.png', speed)
        ]
        elif self.level >= 2.0:            
            self.enemies = [
                Enemy(50, 600, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 200, 50, 50, 'assets/enemy.png', speed)
            ]
        else:
            self.enemies = [
                Enemy(50, 600, 50, 50, 'assets/enemy.png', speed)
            ]
    # Pass in self as a parameter, a method that belongs to the game class so requires self
    # Now can access properties within the class
    def run_game_loop(self):

        player_direction = 0

        while True:
        # Perform the 3 tasks within the loop    
            # Handle Events
            # Query events that pygame provides
            events = pygame.event.get()
            # Events are like keypresses, mouse movement etc
            # For now listen to only pygame.quit, as there are many events have to loop through them
            for event in events:
                if event.type == pygame.QUIT:
                    return # only breaks out of the for in loop
                # when a keyDown event happens
                elif event.type == pygame.KEYDOWN:
                    # check what the key was
                    # only interested in up or donw
                    if event.key == pygame.K_UP:
                        # set direction to -1, up the screen
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        # set direction to +1, down the screen
                        player_direction = +1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
            # therefore put the loop in a function
            # return ends the function so stops the loop          

            # Execute Logic
            # move the player
            self.move_objects(player_direction)
            # introduce a boundary check in player.move


            # Update Display
            self.draw_objects()
            
            # Detect Collisions
            if self.check_collision():
                self.reset_map()



            # update 60 times a second
            # higher tick rate = more updates per second
            self.clock.tick(60)

    def detect_collision(self, obj_1, obj_2):
        # collision when x and and y overlap
        # take into account width and height
        # could have on really long and/or statement if all collision criteria met and false otherwise
        # other solution false on all criteria otherwise true
        # if y position has no collision - above or below
        if obj_1.y > (obj_2.y + obj_2.height):
            return False
        elif (obj_1.y + obj_1.height) < obj_2.y:
            return False
        # if passes these checks, overlap in y position
        # if x position has no collisions
        if obj_1.x > (obj_2.x + obj_2.width):
            return False
        elif (obj_1.x + obj_1.width) < obj_2.x:
            return False
        # if iether fail, overlap in x position

        #if (obj_1.y <= obj_2.y + obj_2.height or obj_1.y + obj_1.height >= obj_2.y) and (obj_1.x <= obj_2.x + obj_2.width or obj_1.x+obj_1.width >= obj_2.x):
        #    return True

        return True

    def draw_objects(self):
        # Fill with white colour then display update
        # Fill with white to overwrite previous drawings in this case
        self.game_window.fill(self.bg_colour)
        # Set the background after filling the background to not overwrite it
        # .blit takes 2 args, the image and a tuple (x_pos, y_pos)
        self.game_window.blit(self.bg.image, (self.bg.x,self.bg.y))

        # 50x50 treasure so 375 puts it 25:25 L:R
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))

        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        
        pygame.display.update()

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height-50)
        for enemy in self.enemies:
            enemy.move(self.width)
    
    def check_collision(self):
        for enemy in self.enemies:            
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False
