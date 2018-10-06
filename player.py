
import arcade


PLAYER_SCALE = 2.3
JUMP_HEIGHT = 15

# player_sprite = arcade.Sprite("res/player.png", PLAYER_SCALE)
# player_sprite.center_x = 100
# player_sprite.center_y = 155

class Player(arcade.Sprite):

    def __init__(self, jumpPos):
        arcade.Sprite.__init__(self, "res/player.png")
        self.center_x = 400
        self.center_y = 150
        self.speed = JUMP_HEIGHT
        self._jumping = True
        self.fittness = 99999999
        self.landingPos = 0
        self.jumpPos = jumpPos
        self.obstacle = None
        self.touched = 1
        self.age = 1

    
    
    def getJumping(self):
        return self._jumping

    def setObstacle(self, obstacle):
        self.obstacle = obstacle
        
    def setJumping(self, value):
        self._jumping = value

    def getJumpPos(self):
        return self.jumpPos
        
    def getFittness(self):
        return self.fittness
        
    def readyToJump(self, obstPos):
        return obstPos - self.center_x <= self.jumpPos
        
    def jump(self):
        if self._jumping:
            self.center_y = self.center_y + self.speed
            if self.speed == -JUMP_HEIGHT:
                self.speed = JUMP_HEIGHT
                self.calculateFittness( self.obstacle.center_x)
                self._jumping = False
                return
            self.speed -= 1
        
    def calculateFittness(self, obstPos):
        self.fittness = abs(self.touched*(self.center_x - obstPos))



            
