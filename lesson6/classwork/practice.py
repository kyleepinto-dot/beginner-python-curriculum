# Problem 1
# Count and print how many time "dog" appears in the list.
pets = ["dog", "cat", "dog", "hamster", "dog", "parrot"]
num_dog = pets.count("dog")
print(num_dog)



# Problem 2
# Count and print how many numbers are odd in the list (a number is odd if it's not divisible by 2).
numbers = [8, 3, 12, 7, 4, 11]
odd_count = sum(1 for n in numbers if n % 2 != 0)

print(odd_count)



# Problem 3
# Search for "monkey" in the list and print its index if it's found.
zoo = ["lion", "elephant", "monkey", "giraffe", "zebra"]
index = zoo.index("monkey")

print(index)



# Problem 4
# Search for 99 in the list and print if it’s found.
numbers = [10, 45, 32, 99, 60, 5]
if 99 in numbers:
    print("Found")



# Problem 5
# Count and print how many numbers are even in the list (a number is odd if it's divisible by 2).
numbers = [13, 22, 8, 19, 6, 7]
even_count = sum(1 for n in numbers if n % 2 == 0)

print(even_count)