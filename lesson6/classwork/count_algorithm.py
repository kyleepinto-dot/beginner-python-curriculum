animals = ["cat", "dog", "cat", "tiger", "lion"]
print(animals)

# You can use built-in Python functions to count some items
num_cats = animals.count("cat")
print("There are", num_cats, "cats")

print("Our algorithm:")

counter = 0
for i in range(len(animals)):  # Go through each item in list
    item = (animals[i])
    if item == "cat": # Check if the item is "cat"
        counter = counter + 1 # If the item is "cat", add 1 to the counter
print(counter, "cats")

numbers = [14, 1, 50, 4, 20, 12]
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers above 10")