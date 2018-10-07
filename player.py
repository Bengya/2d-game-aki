
import arcade
import constants as c




# player_sprite = arcade.Sprite("res/player.png", PLAYER_SCALE)
# player_sprite.center_x = 100
# player_sprite.center_y = 155

class Player(arcade.Sprite):

    def __init__(self, gene):
        arcade.Sprite.__init__(self, "res/player.png")
        self.center_y = 150
        self._jumping = True
        self.fittness = 1000
        self.landingPos = 0
        self.jumpPos = 0
        self.jumpHeight = 0
        self.speed = 0
        self.obstacle = None
        self.touched = 1
        self.age = 0
        self.gene = gene
        
    def generateGene(self, g):
        
        self.gene = g
    
    def calculateJumping(self):
        g = self.gene
        self.jumpPos = g[0][0]*self.obstacle.getSpeed()+g[0][1]*self.obstacle.getWidth()
        self.jumpHeight = g[1][0]*self.obstacle.getSpeed()+g[1][1]*self.obstacle.getWidth()
        self.speed = self.jumpHeight
        
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
        
    def readyToJump(self):
        return self.obstacle.getX() - self.center_x <= self.jumpPos
        
    def jump(self):
        if self._jumping:
            self.center_y = self.center_y + self.speed
            if self.speed <= - self.jumpHeight:
                self.speed = self.jumpHeight
                self.calculateFittness( self.obstacle.center_x)
                self._jumping = False
                return
            self.speed -= 1
        
    def calculateFittness(self, obstPos):
        self.fittness = self.touched*abs(self.center_x - obstPos)



            
