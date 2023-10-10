from turtle import Turtle

# Global variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # Creates the player's turtle character
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.up()
        self.goto(STARTING_POSITION)

    # Moves the player's turtle by MOVE_DISTANCE
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Takes a scoreboard as an input.
    # Brings the user back to STARTING_POSITION and calls the add_level function in the scoreboard class.
    def restart(self, scoreboard):
        self.goto(STARTING_POSITION)
        scoreboard.add_level()
