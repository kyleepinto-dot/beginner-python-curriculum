# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)


# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
fav_animal = input("Enter favorite animal:")
fav_color = input("Enter favorite color:")
print("A",fav_color,fav_animal, "would be awesome!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for num in range(0, 11, 2):
    print(num)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
push_ups = int(input("How many push up can you do?"))
week = push_ups * 7
print("You can do",week,"push ups in a week!")


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for num in range(1,7):
    square = num * num
    print(f"{num}*{num}={square}")
