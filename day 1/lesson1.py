from turtle import * 
speed(15)
width(7)
#we want to draw a house

#step 1: draw a square
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square


#step 2: draw a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#step 3: draw a roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#step 4:draw windows
penup()
goto(30,170)
pendown()
color("blue")
begin_fill()
right(150)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
goto(130,130)
pendown()
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()
exitonclick()