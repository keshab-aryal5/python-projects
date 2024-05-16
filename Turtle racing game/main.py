from turtle import Screen,Turtle
import random
screen = Screen()
screen.title("b12F_msh")
screen.bgcolor("black")
screen.screensize(500,500)
turtle_list = []
x_cor = -345
y_cor = -160
turtle_color =["red","green","blue","yellow","purple","orange","white","pink","brown","grey"]
for i in range(len(turtle_color)):
    tim = Turtle(shape="turtle")
    tim.color(turtle_color[i])
    tim.pu()
    tim.goto(x_cor,y_cor)
    turtle_list.append(tim)
    y_cor += 40


ans = screen.textinput(title="Make your bet",prompt="Which turtle will win the race ").lower()
winner = ""
if ans:
    keep_going = True
else:
    keep_going = False
while keep_going:
    obj = random.choice(turtle_list)
    obj.fd(random.randint(0,10))

    if obj.xcor() >= 350:
        obj.setheading(180)

    if obj.xcor() <= -350:
        winner = obj.color()
        keep_going = False


if winner == ans:
    print(f"Yeah!!! you guessed it right {winner[0]} turtle is winner")
else:
    print(f"Oh no {ans} turtle isn't winner. The winner is {winner[0]} turtle")

screen.exitonclick()