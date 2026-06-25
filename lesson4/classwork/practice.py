# Problem 1
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."
age = int(input())
height = float(input())

if age >= 10 and height >= 120:
    print("You can ride!")
else:
    print("Sorry, you can't ride.")


# Problem 2
# Generate a random number between 1 and 5.
# Ask the user to guess.
# If they guessed right OR the number is 3, print "Lucky!"
# Otherwise, print "Not today."
import random

secret_number = random.randint(1, 5)
guess = int(input())

if guess == secret_number or secret_number == 3:
    print("Lucky!")
else:
    print("Not today.")


# Problem 3
# Ask the user to enter 3 numbers.
# If NOT all of them are even (meaning at least one is odd), print "Odd one detected!"
# Otherwise, print "All even!"
num1 = int(input())
num2 = int(input())
num3 = int(input())

if not (num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0):
    print("Odd one detected!")
else:
    print("All even!")



# Problem 4
# Ask if the user has a membership and if they scored 100 points in a game.
# If they have a membership OR scored 100, print "You earned a bonus pass!"
# Otherwise, print "No bonus pass."
has_membership = input().strip().lower() == "yes"
points = int(input())

if has_membership or points == 100:
    print("You earned a bonus pass!")
else:
    print("No bonus pass.")


# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."
num = int(input())

if num % 3 == 0 and (num < 0 or num > 100):
    print("Weird number!")
else:
    print("Normal number.")