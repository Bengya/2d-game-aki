from player import Player
import random
import constants as c

POPULATION =    c.POPULATION
FIRSTPOS =      c.FIRSTPOS
ENDPOS   =      c.SCREEN_WIDTH - 50
class CactusJumperGenerator():
    def __init__(self):
        self.population = []
        self.obstacle = None
        self.startPos = [x for x in range(FIRSTPOS,ENDPOS,100)]
        
        
    def populate(self):
        
        for i in range(POPULATION - len(self.population)):
            a = random.uniform(0.0, 2.0)
            b = random.uniform(0.0, 2.0)
            c = random.uniform(0.0, 0.5)
            d = random.uniform(0.0, 0.5)
            gene = [[a,b], [c,d]]
            self.population.append(Player(gene))
        self.sortByFittness()    
        for player in self.population:
            player.age += 1
            player.setObstacle(self.obstacle)
            player.calculateJumping()
            player.setJumping(True)
        self.rePos()
            
    def selection(self):
        
        self.sortByFittness()
        breedList = self.population[:9]
        
        for i in range(0,len(breedList)-1,2):
            g1,g2 = self.crossGene(breedList[i].gene, breedList[i+1].gene)
            breedList[i].generateGene(g1)
            breedList[i+1].generateGene(g2)
            
        self.population = breedList
    def crossGene(self,g1,g2):
        a = g1[0][0]
        b = g1[0][1]
        c = g1[1][0]
        d = g1[1][1]
        e = g2[0][0]
        f = g2[0][1]
        g = g2[1][0]
        h = g2[1][1]
        c1 = [a,e]
        c2 = [b,f]
        c3 = [c,g]
        c4 = [d,h]
        ng1 = [[random.choice(c1),random.choice(c2)],[random.choice(c3),random.choice(c4)]]
        ng2 = [[random.choice(c1),random.choice(c2)],[random.choice(c3),random.choice(c4)]]
        return ng1,ng2

    
    def rePos(self):
        for i in range(len(self.population)):
            self.population[i].center_x = self.startPos[i]
            self.population[i].center_y = 150
            
    def jumpingFinished(self):
        list = [i.getJumping() for i in self.population]
        return not any(list)
        
    def sortByFittness(self):
        self.population.sort(key=lambda x : x.getFittness())
        
    
        
        
            
            
        
        