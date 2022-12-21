#ORION
import turtle
turtle.speed(1)
turtle.bgcolor('gray')
turtle.penup()
turtle.setup(500,600)
#STARS
LEFT_SHOUlDER_X = -70
LEFT_SHOUlDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

#APPLY_THE_STARS

turtle.goto(LEFT_SHOUlDER_X,LEFT_SHOUlDER_Y)
turtle.dot('blue')
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.dot('red')
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.dot('purple')
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.dot('cyan')
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.dot('brown')
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.dot('yellow')
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.dot('pink')


#print_the_name_of_the_stars

turtle.up()
turtle.hideturtle()
turtle.goto(LEFT_SHOUlDER_X,LEFT_SHOUlDER_Y)
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.write('Минтака')
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.write('Саиф')
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.write('Ригель')

#
turtle.goto(LEFT_SHOUlDER_X,LEFT_SHOUlDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.penup()

#
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.penup()

#
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.penup()
#
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.penup()
#
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.penup()
#
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.penup()


turtle.done()