# Coin collection simulator using the arcade library

import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_COIN = 0.5
COIN_COUNT = 20


class MyGame(arcade.Window):
    # custom window class

    def __init__(self):
        # initializes new variables
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Coin Collector")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up the game and initialize the variables

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("sprite_yusuf.png", SPRITE_SCALING_PLAYER)  # "Yusuf" by K. Cevik on MS Paint
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            coin = arcade.Sprite("british_coin.png", SPRITE_SCALING_COIN)  # Coin image sourced from "Bristol Live" site

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        # Draw the sprite lists here
        self.coin_list.draw()
        self.player_list.draw()

        # Display the text visibly on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        # Handle mouse motion

        # Move the center of the player sprite to match the mouse
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE or arcade.key.Q:
            arcade.close_window()


def main():
    # Main Method
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
