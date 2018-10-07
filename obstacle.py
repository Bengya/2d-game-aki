import arcade
import constants as c

SPRITE_SCALING_OBSTACLE = 50.0/arcade.load_texture("res/obstacle.png").width

class Obstacle(arcade.Sprite):
    
    def __init__(self, speed):
        arcade.Sprite.__init__(self, "res/obstacle.png", SPRITE_SCALING_OBSTACLE)
        self.speed = speed
        self.center_x = c.SCREEN_WIDTH 
        self.center_y = 125
        
    def getX(self):
        return self.center_x
        
    def getY(self):
        return self.center_y
    
    def getSpeed(self):
        return self.speed
    def getWidth(self):
        return self.width
    def move(self):
        self.center_x -= self.speed
        
        
    
        