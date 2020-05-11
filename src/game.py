#Pillagers
import turtle
import os

#Set up the screen
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Pillagers")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("blue")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.50,.50)
bullet.hideturtle

bulletspeed = 20

#define bullet state
#ready to fire
bulletstate = "ready"
#fire

#Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)

	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	#declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
	#move bullet to just above player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()


#Create keyboard bindings
turtle.Screen().listen()
turtle.Screen().onkey(move_left, "Left")
turtle.Screen().onkey(move_right, "Right")
turtle.Screen().onkey(fire_bullet, "space")

#game Loop
while True:
	
	#move the enemy
	x = enemy.xcor()
	x += enemyspeed
	enemy.setx(x)

	#move enemy back and down
	if enemy.xcor() > 280:
		enemyspeed *= -1
		y = enemy.ycor()
		y -= 40
		enemy.sety(y)


	if enemy.xcor() < -280:
		enemyspeed *= -1
		y = enemy.ycor()
		y -= 40
		enemy.sety(y)

	#move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#check to see if bullet is gong
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"