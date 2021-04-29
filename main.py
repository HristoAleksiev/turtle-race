from turtle import Turtle, Screen
import random as r

scr = Screen()
scr.setup(width=1000, height=800)
STARTING_X_POSITION = -470
STARTING_Y_POSITION = -200
racing_turtles = []
turtle_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Black", "Brown"]
player_bet = scr.textinput(title="Bet on a Turtle and win Big!",
                           prompt="Which turtle do you think will win the race: "
                                  f"({', '.join(turtle_colors)})")


def check_if_winner(racers):
    for _ in racers:
        position = _.position()
        if position[0] >= 385:
            return _
    return False


def run_race(racers):
    winner = False
    while winner is False:
        for turtle in racers:
            turtle.forward(r.randint(10, 20))

        winner = check_if_winner(racers)
    return winner


def check_bet(player_bet, winner_racer):
    winner_color = winner_racer.color()[0]
    if player_bet == winner_color:
        print(f"You are a lucky man, the winner was indeed: {winner_color}")
    else:
        print(f"That is too bad, the actual winner is {winner_color}")


def initialize_race(turtle_colors, starting_x, starting_y):
    for color in turtle_colors:
        turtle_racer = Turtle(shape="turtle")
        turtle_racer.color(color)
        turtle_racer.penup()
        turtle_racer.shapesize(stretch_wid=3, stretch_len=3)
        racing_turtles.append(turtle_racer)

    for racer in racing_turtles:
        racer.goto(x=starting_x, y=starting_y)
        starting_y += (scr.window_height() - 300) / len(racing_turtles)


initialize_race(turtle_colors, STARTING_X_POSITION, STARTING_Y_POSITION)
winner_turtle = run_race(racing_turtles)
check_bet(player_bet, winner_turtle)

scr.exitonclick()
