import turtle as turtle
import random

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  for i in range(0, 5):
      turtle.pencolor("pink")
      turtle.forward(110)
      turtle.left(216)

def square():
  for i in range(0, 4):
      turtle.pencolor("green")
      turtle.forward(100)
      turtle.right(90)

def hexagon():
  for i in range(0, 6):
      turtle.pencolor("red")
      turtle.forward(60)
      turtle.right(60)

def rectangle():
    for i in range(0, 2):
      turtle.pencolor("orange")
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(60)
      turtle.right(90)

selection = input("1. Star\n2. Square\n3. Hexagon\n4. Rctangle\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
elif selection == "4":
  print("Excellent choice! Go to the result tab to see your creation.")
  rectangle()
