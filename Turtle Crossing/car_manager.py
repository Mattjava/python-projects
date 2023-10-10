from turtle import Turtle
import random

# Global variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # Creates the list of cars in the car manager
    def __init__(self):
        self.listOfCars = []

    # Creates a car turtle and puts it in the car manager's list of cars
    def make_car(self):
        new_coordinate = (300, random.randint(-250, 250))

        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_len=3, stretch_wid=1)
        new_car.up()
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.goto(new_coordinate)
        self.listOfCars.append(new_car)

    # Takes the current level as an input
    # Moves all the cars on screen by the move variable.
    # Move can be incremented by MOVE_INCREMENT each time the user passes a level
    def move_cars(self, level):
        move = STARTING_MOVE_DISTANCE
        if level > 1:
            for i in range(level-1):
                move += MOVE_INCREMENT

        for car in self.listOfCars:
            car.forward(move)

