from turtle import*

# we whant to paint a house
#step 1:  draw a square
shape("turtle")
#speed(9)
width(7)
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


forward(70)
color("yellow")
left(90)
forward(120)      # height of the door
right(90)
forward(60)
right(90)
forward(120)




begin_fill
penup()
goto(150, 150)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(10, 150)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(195)
left(119)
forward(195)
end_fill()











exitonclick()




