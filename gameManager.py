import obstacle
import arcade
import os

from player import Player


SCREEN_WIDTH    = 1200
SCREEN_HEIGHT   = 500

class GameManager(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.obstacle_list = None

        self.player = Player()
        self.player.Jumping = False

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)
        
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.obstacle_sprite = obstacle.Obstacle(0.1)
        self.obstacle_sprite.center_x = 1175
        self.obstacle_sprite.center_y = 125
        self.obstacle_list.append(self.obstacle_sprite)

        # Create the coins
        
    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.obstacle_list.draw()
        arcade.draw_line(0, 100, 1200, 100, arcade.color.BLACK, 2)

        texture = arcade.load_texture("res/dirt.png")
        scale = .25
        
        for i in range(50, 1200, 100):
            arcade.draw_texture_rectangle(i, 50, scale * texture.width,
                              scale * texture.height, texture, 0)
    def update(self, delta_time):
    
        for obstacle in self.obstacle_list:
            obstacle.move()
            
        self.obstacle_list.update()
def main():
    """ Main method """
    window = GameManager()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()       