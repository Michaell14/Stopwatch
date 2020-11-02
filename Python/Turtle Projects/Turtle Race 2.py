import turtle
import random
width=700
height=500

S=turtle.Screen()
S.setup(width, height)
S.bgcolor('lightgreen')

#Create pen
T=turtle.Turtle()
T.speed(0)

#Startline
T.up()
T.setposition(-140, 50)
T.write("Start line", align='center')
T.right(90)
T.forward(10)
T.down()
T.forward(155)

#Finish line
T.up()
T.setposition(140, 50)
T.write("Finish line", align='center')
T.forward(10)
T.down()
T.forward(155)

#Track lines
T.left(90)
startYPosition=20
for trackLine in range(5):
    T.up()
    T.setposition(-170, startYPosition)
    T.color("white")
    T.down()
    T.forward(340)
    startYPosition=startYPosition-30

T.hideturtle()


T1=turtle.Turtle()
T1.up()
T1.setposition(-160, 10)
T1.shape("turtle")
T1.color("red")

T2=turtle.Turtle()
T2.up()
T2.setposition(-160,-20)
T2.shape("turtle")
T2.color("green")

T3=turtle.Turtle()
T3.up()
T3.setposition(-160, -50)
T3.shape("turtle")
T3.color("blue")

T4=turtle.Turtle()
T4.up()
T4.setposition(-160, -80)
T4.shape("turtle")
T4.color("yellow")

line=140
while T1.xcor()<line or T2.xcor()<line or T3.xcor()<line or T4.xcor()<line:
    T1.forward(random.randint(1,5))
    T2.forward(random.randint(1,5))
    T3.forward(random.randint(1,5))
    T4.forward(random.randint(1,5))


#Decide ranking 
finals_list=[T1.xcor(), T2.xcor(), T3.xcor(), T4.xcor()]
finals_dict={T1.xcor(): 'red', T2.xcor(): "green", T3.xcor(): "blue", T4.xcor(): 'yellow'}

finals_list=sorted(finals_list, reverse=True)


#Ranking Board
T.up()
T.color("Black")
T.setposition(-60, 200)
T.write("Ranking Board", align="left", font=(None, 12))
T.setposition(-60, 180)
T.write("1st place: "+finals_dict[finals_list[0]], align="left")
T.setposition(-60, 160)
T.write("2nd place: %s turtle" %turtle2, align='left')


    
