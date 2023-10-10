import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen settings

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Chance
# Controls how often the cars will spawn
# Will decrease by 1 each time the player finishes a level
# Will stop at 1 to provide the highest chance of a car spawning.
chance = 5

# Objects
player = Player()
manager = CarManager()
scoreboard = Scoreboard()


# Screen listening
# Allows the player to control their turtle
screen.listen()
screen.onkey(fun=player.move, key="w")
screen.onkey(fun=player.move, key="Up")

# While loop that'll run the game while game_is_on is true
# Will stop if the player hits one of the cars

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Controls the spawn rate of the cars
    if random.randint(0, chance) == 0:
        manager.make_car()
    # Moves the cars
    manager.move_cars(scoreboard.level)

    # Updates the screen
    screen.update()

    # Checks if the player has crashed into one of the cars
    for car in manager.listOfCars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over_sequence()

    # Checks if the player has reached the finish line.
    if player.ycor() >= 280:
        player.restart(scoreboard)
        if chance > 1:
            chance -= 1

# The end code.
screen.exitonclick()
