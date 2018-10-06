from player import Player
import random
import constants as gm

POPULATION = gm.POPULATION
FIRSTPOS = gm.FIRSTPOS
ENDPOS   = gm.SCREEN_WIDTH - 50
class CactusJumperGenerator():
    def __init__(self):
        self.population = []
        self.obstacle = None
        self.startPos = [x for x in range(FIRSTPOS,ENDPOS,100)]
        
        
    def populate(self):
        for i in range(POPULATION - len(self.population)):
            self.population.append(Player(random.randint(0,1000)))
        for player in self.population:
            player.setObstacle(self.obstacle)
        self.rePos()
            
    def selection(self):
        
        self.population.sort(key=lambda x : x.getFittness())
        breedList = self.population[:9]
        newList = breedList
        for i in range(0,len(breedList)-1,2):
            avg = (breedList[i].jumpPos + breedList[i+1].jumpPos)/2
            newList[i].jumpPos = avg
        self.rePopulate(newList[0:5])
        
    def rePopulate(self, breedList):
        newMember = POPULATION - len(breedList)
        for i in breedList:
            i.age += 1
        for _ in range(newMember):
            breedList.append(Player(random.randint(0,100)))
            self.population = breedList
            self.rePos()
        for obj in self.population:
            obj.setJumping(True)
    
    def rePos(self):
        for i in range(len(self.population)):
            self.population[i].center_x = self.startPos[i]
        
        
            
            
        
        