import arcade
import os
import random


from artificial import CactusJumperGenerator
from obstacle import Obstacle
from player import Player

import constants as c



class GameManager(arcade.Window):
    def __init__(self):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "Sprite Example")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.obstacle_list = None
        self.set_update_rate(1/200)
        self.gameRunning = True
        self.counter = 0

        self.generation = CactusJumperGenerator()

        # Set up the player info
        self.player_sprite = None
        self.score = 1

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)
        
    def setup(self):
        """ Set up the game and initialize the variables. """
        obsSpeed = random.uniform(7,11)
        obsWidth = random.uniform(30,50)
        # Sprite lists
        self.obstacle = Obstacle(obsSpeed)
        self.obstacle.width = obsWidth
        self.generation.obstacle = self.obstacle
        self.generation.populate()
        self.player_list = arcade.SpriteList()

        # Score

        # Set up the player
        # Character image from kenney.nl

        
        for sprite in self.generation.population:
            self.player_list.append(sprite)

        self.fitList = [player.getFittness() for player in self.player_list]

        # Create the coins
        
    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.obstacle.draw()
        self.player_list.draw()
        
        
        arcade.draw_line(0, 100, c.SCREEN_WIDTH, 100, arcade.color.BLACK, 2)
        
        texture = arcade.load_texture("res/dirt.png")
        scale = .25
        
        for i in range(50, c.SCREEN_WIDTH, 100):
            arcade.draw_texture_rectangle(i, 50, scale * texture.width,
                              scale * texture.height, texture, 0)
        
                              
        output = f"Generation: {self.score}"
        arcade.draw_text(output, 600, 450, arcade.color.WHITE, 14)
        output2 = str(self.fitList)
        arcade.draw_text(output2, 100, 450, arcade.color.WHITE, 14)
        
        for p in self.player_list:
            o = "G:" + str(p.age)
            o2 = "F: %.2f" %p.getFittness()
            o3 = "JP: %.2f" %p.jumpPos
            o4 = "JH: %.2f" %p.jumpHeight
            o5 = "%.2f" % (p.gene[0][0])
            o6 = "%.2f" % (p.gene[0][1])
            o7 = "%.2f" % (p.gene[1][0])
            o8 = "%.2f" % (p.gene[1][1])
            arcade.draw_text(o, p.center_x, p.center_y+30, arcade.color.WHITE, 14)
            arcade.draw_text(o2, p.center_x, p.center_y+10, arcade.color.WHITE, 14)
            arcade.draw_text(o3, p.center_x, p.center_y-10, arcade.color.WHITE, 14)
            arcade.draw_text(o4, p.center_x, p.center_y-30, arcade.color.WHITE, 14)
            arcade.draw_text(o5, p.center_x - 20, p.center_y+80, arcade.color.WHITE, 8)
            arcade.draw_text(o6, p.center_x - 20, p.center_y+70, arcade.color.WHITE, 8)
            arcade.draw_text(o7, p.center_x - 20, p.center_y+60, arcade.color.WHITE, 8)
            arcade.draw_text(o8, p.center_x - 20, p.center_y+50, arcade.color.WHITE, 8)
        
    def update(self, delta_time):
    
        # if not self.obstacle_list:
            # self.obstacle_list.append(Obstacle(OBSTACLE_SPEED))
            
        # elif NEW_OBSTACLE_PER_FRAME > random.randint(0,100) and self.obstacle_list[-1].center_x <= 900:
            # self.obstacle_list.append(Obstacle(OBSTACLE_SPEED))
        self.counter+=1
        print(self.counter)
        self.obstacle.move()
        
        for player in self.player_list:
            if player.readyToJump():
                player.jump()
            
        hit_list = arcade.check_for_collision_with_list(self.obstacle, self.player_list)
        for player in hit_list:
            player.touched = 1000
        self.player_list.update()
        self.obstacle.update()
        

            
        # Loop through each colliding sprite, remove it, and add to the score.
        if self.generation.jumpingFinished() and self.obstacle.center_x < 10:
            self.generation.selection()
            self.score += 1
            self.setup()
        
        
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.SPACE:
            pass
            
            
    # def endGame(self):
        
            
def main():
    """ Main method """
    window = GameManager()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()       