import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
oplist = ["Windows", "Mac", "iPhone"]
print(oplist[len(oplist) - 1])
oplist.reverse()
print(oplist)



# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["Mathematics", "History", "Biology", "Art"]
print(subjects[1])
subjects.sort()
print("After sort:", subjects)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_codes = ["200", "400", "403", "404", "500"]
print(len(error_codes))
print(error_codes.index("403"))


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random

languages = ["Python", "JavaScript"]
print(random.choice(languages))
languages.append("Go")
print(languages)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["pass1", "pass2", "pass3", "pass4", "pass5", "pass6"]
print(passwords[len(passwords) // 2])
print(passwords.pop(0))