from turtle import Turtle, Screen
import random
import time

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True
    
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    
    while is_race_on:
        for t in all_turtle:
            if t.xcor() > 225:
                is_race_on = False
                winning_color = t.pencolor()
                if winning_color == user_bet:
                    time.sleep(2)
                    screen.clear()
                    pen.goto(-180,0)
                    pen.write(f"You've won! The {winning_color} turtle has won the race.", font=("Arial", 10, "bold"))
                else:
                    time.sleep(2)
                    screen.clear()
                    pen.goto(-180,0)
                    pen.write(f"You've lost! The {winning_color} turtle has won the race.", font=("Arial", 10, "bold"))
            rand_distance = random.randint(0, 10)
            t.forward(rand_distance)


screen.exitonclick()

