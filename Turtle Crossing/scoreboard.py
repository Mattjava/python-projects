from turtle import Turtle

# Global variables.
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # Sets up the turtle that'll create the scoreboard
    # Creates an attribute that'll hold the current level the player is in
    # Makes that turtle write the current level
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.up()
        self.draw_level()

    # Makes the turtle write the current level in the upper-left corner of the screen
    def draw_level(self):
        self.goto(-200, 250)
        self.clear()
        self.write(f"Level {self.level}", False, "center", FONT)

    # Adds a level to the level attribute and updates the level scoreboard
    def add_level(self):
        self.level += 1
        self.draw_level()

    # Draws the level scoreboard, goes to the center, and writes "Game Over" in it.
    def game_over_sequence(self):
        self.draw_level()
        self.goto(0, 0)
        self.write("Game Over", False, "center", FONT)
