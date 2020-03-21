#Salim Stanbury
#Prof. Vanselow
#Integration Project

print("Hello my name is Salim Stanbury")
print("Welcome to my integraton project!")
a = input("Enter your name: ")
print("Hello , " + a + "!")
print("How are you ?")
input()
print("I am doing well thanks for asking ,lol ")
print("It has been cold recently, what is the weather today ?")
weather = input("Enter the weather: ")
print("Dress appropriateley :)")
job = input("Do you have a job: ")
income = int(input("How much do you make per week: "))
print( income * 4 , "dollars is your monthly income")
expense1 = int(input("How much money would you say you spend on food per week: "))
if expense1 >= 150:
    print("You need to cut it down")
elif expense1 < 150:
    print("Great saving")
drink = 20
meal = 45
dessert = 25
dinner = drink + meal + dessert
print("Dinner will cost $90 per person")
bev = int(input("How many drinks would you order: "))
print( bev * 20 , "dollars would be your expense on drinks")
eat = int(input("How many meals would you order: "))
print( eat * 45 , "dollars would be your expense on meals")
num1 = int(input("Type a number 1-10: "))
mod = num1 % 2
if mod > 0:
    print("This is a odd number")
else :
    print("This is an even number")
print("Add 5 to this number")
print("Now add 6 to this number")
guess = input("Done ?: ")
print("Subtract the number", num1, "you originally chose")
print("Your new number is 11")
c = int(input("Enter a two-digit integer: "))
print("What would the inverse of these numbers be ?")
d = (str(c % 10) + str(c // 10))
print(d)
print("Beat you to it :)")
age = int(input("How old are you: "))
if age > 50:
    print("You have aged well ")
elif age >= 20 and age <= 50:
    print("You are in your prime years")
elif age < 20:
    print("You have plenty more years to have fun")
edu = input("What school do you attend: " )
print(edu, "?" " Oh wow I love that school! ")

rate = int(input("Rate our conversation, 1-10: "))
if rate >= 6:
    print("Thank you have a wonderful day :)")
elif rate < 6:
    print("Maybe you need to work on your people skills :(")
57
color = input("Enter your favorite color: ")
x = 0
while(x < 3):
    print(color)
    x = x+ 1
howMany = input("Did you see it 3 times? ")

favorite = input("Enter your favorite brand: ") 
for x in range(1,4): 
       print(str(x) + ".", favorite, end="\t")
       print("  ")
diff = input("Spot a difference between the two lists? ")
print("Let's do some math!Enter a number below, ill tell you if it's a perfect square")
import math
number = int(input())

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print("perfect square")
else:
    print("not a perfect square")
doAgain = True
while doAgain:
    You = int(input("Enter your age: "))
    Mom = int(input("Ener your mothers age: "))
    print("P.S. if you don't have one..... make the age up")
    Dad = int(input("Enter your fathers age: "))
    yourSibling = int(input("Enter siblings age: "))
    maxNum1 = max(You, Mom, Dad, yourSibling)
    print("The oldest person in your family is", maxNum1)
    another = input("Type 'R' to recalculate "+"or any other key to exit.")

    if another != 'R':
        doAgain = False
print("Your welcome!")

print("Let's find the area in inches of your computer screen")
#  Area of a Rectangle
width = float(input('Enter the approx Width of the Rectangle screen: '))
height = float(input('Enter the approx Height of the Rectangle screen: '))
Area = width * height
Perimeter = 2 * (width + height)

print("Area of the screen is: %.2f" %Area)
print("Perimeter of screen is: %.2f" %Perimeter)

print("Let's do some magic, youll be given a card and dont tell anyone")
ready =input("Press enter when ready")
def card_function():
  import random
  number = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
  print(number[random.randint(0, 13)] + " of " + suits[random.randint(0, 3)])
card_function()
print("The trick is continued on the next integration:) ")
print("Thank you, stay safe from corona! ")
