# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
number = int(input("Enter a number: "))
if number % 2 == 0:
  print("Even")
else:
  print("Odd")
# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day_of_week = input("Enter the date:").lower()
if day_of_week == "sunday" or "saterday":
    print("Weekend")
else:
   print("Weekday")
# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random

def guess_number():
    secret_number = random.randint(1, 10)

    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            return

        if guess == secret_number:
            print("Correct!")
        else:
            print(f"Try again! The number was {secret_number}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guess_number()



# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria."
nums = int(input("Enter a positive number:"))
if nums % 2 == 0 and nums > 10:
    print("Big even number.")
else:
    print("Number does not meet criteria.")





# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))
if num_1 > num_2:
    print("First number is bigger.")
elif num_2 > num_1:
    print("Second number is bigger.")
else:
    print("Numbers are equal.")