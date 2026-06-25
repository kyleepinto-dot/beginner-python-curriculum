# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]

alex_count = names.count("Alex")
print('The name "Alex" appears:', alex_count, "times")



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]

if "elephant" in animals:
    print("Elephant is found!")
else:
    print("Elephant is not found.")



# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]

count = names.count("100")
print('The number 100 appears:', count, "times")





# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]

if "blue" in colors:
    print(colors.index("blue"))



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]

count = 0
for temp in temperatures:
    if temp < 0:
        count += 1

print(count)