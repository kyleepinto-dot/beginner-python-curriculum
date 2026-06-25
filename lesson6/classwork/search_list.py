fruit = ["banana", "apple"]

# Find if apple in list
if "apple" in fruit:
    print("Found apple")
else:
    print("No apples found")

print("Our algorithm:")

# Find if apple in list and print its index

found = False
index = -1

for i in range(len(fruit)):  # Go through each item in the list
    if fruit[i] == "apple":  # If the current item is apple
        found = True  # Mark as found
        index = i  # Save the index
        break  # Exit the loop after finding

if found == True:
    print("Found apple at", index)
else:
    print("No apples in the list")