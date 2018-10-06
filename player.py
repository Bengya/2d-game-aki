
import arcade


PLAYER_SCALE = 2.3

# player_sprite = arcade.Sprite("res/player.png", PLAYER_SCALE)
# player_sprite.center_x = 100
# player_sprite.center_y = 155

class Player(arcade.Sprite):

    def __init__(self):
        arcade.Sprite.__init__(self, "res/player.png", PLAYER_SCALE)
        self.center_x = 100
        self.center_y = 155
        self.speed = 12
        self._jumping = False

    
    
    def getJumping(self):
        return self._jumping


    def setJumping(self, value):
        self._jumping = value

    
    
    def jump(self):
        self.center_y = self.center_y + self.speed
        if self.speed == -12:
            self.speed = 12
            self._jumping = False
            return
        self.speed -= 1



            
