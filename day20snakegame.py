from turtle import Screen,Turtle, width
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
starting_position=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in starting_position:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

game_is_on=True
while game_is_on:
    for seg in segments:
        seg.forward(20)




screen.exitonclick()