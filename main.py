import turtle
import math 
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(turtle=None):
  turtle.up()
  turtle.goto(0,0)
  for i in range(-360,360):
    y =math.sin(math.radians(i))
    turtle.goto(i,y)
    turtle.down()
def setupWindow(wn=None):
  turtle.setworldcoordinates(-360, 1, 360, -1)
def setupAxis(dart):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  dart.goto(360,0)
  dart.goto(0,0)
  dart.goto(0,1)
  dart.goto(0,-1)
def drawCosineCurve(turtle=None):
  turtle.up()
  turtle.goto(0,0)
  for i in range(-360,360):
    y =math.cos(math.radians(i))
    turtle.goto(i,y)
    turtle.down()
def drawTangentCurve(turtle=None):
  turtle.up()
  turtle.goto(0,0)
  for i in range(-360,360):
    y =math.tan(math.radians(i))
    turtle.goto(i,y)
    turtle.down()





##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
