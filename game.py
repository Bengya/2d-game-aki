

import arcade
import os
import obstacle
# Set the working directory (where we expect to find files) to the same
# directory this .py file is in. You can leave this out of your own
# code, but it is needed to easily run the examples using "python -m"
# as mentioned at the top of this program.
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

arcade.open_window(1200, 500, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Draw a grid
# Draw vertical lines every 120 pixels


# Draw horizontal lines every 200 pixels

arcade.draw_line(0, 100, 1200, 100, arcade.color.BLACK, 2)

texture = arcade.load_texture("res/dirt.png")
scale = .25

for i in range(50, 1200, 100):
	arcade.draw_texture_rectangle(i, 50, scale * texture.width,
                              scale * texture.height, texture, 0)
                              
                              

obstacle = obstacle.Obstacle(0)

# Finish the render.
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()