# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]

total = 0
for num in numbers:
    if num > 25:
        total += num

print(total)

# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]

total = 0
for num in numbers:
    if num < -10:
        total += num

print(total)


# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]

max_num = float('-inf')
for num in numbers:
    if num < 100 and num > max_num:
        max_num = num

print(max_num)


# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]

max_num = float('-inf')
for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)



# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]

total = 0
for num in numbers:
    total += num

print(total)