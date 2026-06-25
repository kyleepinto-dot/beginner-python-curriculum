import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
cars = ["Toyota", "Ford", "Honda", "BMW"]
print(cars[0], cars[-1])
cars.append("Tesla")
print(cars)


# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
numbers.insert(2, 99)
print(numbers)


# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then remove one city and print the updated list.
cities = ["Tokyo", "Paris", "New York"]
print(len(cities))
cities.remove("Paris")
print(cities)


# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
import random

extensions = ["txt", "pdf", "jpg", "png", "py", "csv"]
print(random.choice(extensions))
extensions.pop(3)
print(extensions)


# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then count how many times a specific name appears.
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Bob", "Frank", "Grace"]
print(names[len(names) // 2])
print(names.count("Bob"))