import turtle
import random

turtles = list()

# cheating turtle
class SuperTurtle(turtle.Turtle):
    def forward(self, distance):
        cheat_distance = distance + 5
        turtle.Turtle.forward(self, cheat_distance)
        
# Set up game
# create a few turtles,each with its own color and position on the starting line.
def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290,720)
    screen.bgpic('pavement.gif')

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green']

    for i in range(0, len(turtle_ycor)):
##        if i == 4:
##            new_turtle = SuperTurtle()
##        else:
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)



# Start the race
# Set a variable winner to False
# while winner is False, Pick a random amount to move forward.
# Check to see if turtle’s position is across finish line
# Set winner to True
def race():
    global turtles
    winner = False
    finishline = 570

    while not winner:
        for current_turtle in turtles:
            move = random.randint(0,2)
            current_turtle.forward(move)

            xcor = current_turtle.xcor()
            if xcor >= finishline:
                # Game finishes
                # Announce the winner's name
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0], 'turtle')
                

setup()
race()

turtle.mainloop()
