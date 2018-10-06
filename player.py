
import arcade


PLAYER_SCALE = 2.3

# player_sprite = arcade.Sprite("res/player.png", PLAYER_SCALE)
# player_sprite.center_x = 100
# player_sprite.center_y = 155

class Player(arcade.Sprite):

    def __init__(self):
        arcade.Sprite.__init__(self, "res/player.png", PLAYER_SCALE)
        self.center_x = 100
        self.ceter_y = 155
        self.speed = 12
        self._jumping = False

    
    @property
    def Jumping(self):
        return _jumping

    @Jumping.setter
    def Jumping(self, value):
        self._jumping = value

    
    
    def jump(self):
        if self.center_y == 155:
            if self.speed == -12:
                self.speed = 12
                self._jumping = False
                return

            self.center = self.center - self.speed
            self.speed -= 1


            
