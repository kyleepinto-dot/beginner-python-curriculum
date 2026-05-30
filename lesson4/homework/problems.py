# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test_1 = int(input("Enter 1st test score:"))
test_2 = int(input("Enter 2nd test score:"))
if test_1 >= 50 and test_2 >= 50:
    print("You passed both!")
else:
    print("You failed at least one.")



# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("Did you bring lunch? (yes/no): ").strip().lower()
water = input("Did you bring water? (yes/no): ").strip().lower()

if lunch == "yes" and water == "yes":
    print("You're fully ready!")
elif lunch == "yes" or water == "yes":
    print("You're somewhat ready.")
else:
    print("You're not ready.")




# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
nums = int(input("Enter a number:"))
if nums in range(1,11,1):
    print("In range.")
else:
    print("Out of range.")



# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number and secret_number % 2 == 0:
    print("Even match!")
elif guess == secret_number or secret_number == 5:
    print("Nice try!")
else:
    print("Nope.")


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

cond1 = (num1 % 5 == 0 and num2 % 2 != 0)
cond2 = (num2 % 5 == 0 and num1 % 2 != 0)

if cond1 or cond2:
    print("Interesting pair!")
else:
    print("Plain pair.")