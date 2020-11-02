import turtle
width=700
height=500
S=turtle.Screen()
S.setup(width, height)
S.bgcolor("lightgreen")
T=turtle.Turtle()
T.speed(0)
T.up()
T.setposition(-140, 50)
T.write("Start line", align="center")
T.right(90)
T.forward(10)
T.down()
T.forward(155)
T.up()
T.setposition(140,50)
T.write("Finish line", align="center")
T.forward(10)
T.down()
T.forward(155)
T.up()
setYPos=25
T.left(90)
for i in range(5):
    T.setposition(-170, setYPos)
    T.color("white")
    T.down()
    T.forward(340)
    T.up()
    setYPos=setYPos-30
