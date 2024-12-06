# 1. Print List
# Part A
def printList(p):
    print(" ".join(p))                                                    # Joins the elements of the list `p` with spaces and prints them

# Part B
def main():
    lst = ["apple", "banana", "cherry"]                                   # Creates a list of strings
    printList(lst)                                                        # Calls the printList function to display the list

# Part C
main()

print("")

# Data Management Functions
# 2. Name format
# Part A
def nameFormat(first, middle, last):
    print(f"{first.title()} {middle[0].upper()}. {last.title()}")         # Formats the name with proper capitalization and a middle initial

# Part B
def main():
    nameFormat("john", "stu", "smith")                                    # Calls the nameFormat function using positional arguments
    nameFormat(first="john", middle="fitzgerald", last="kennedy")         # Calls the nameFormat function using keyword arguments

# Part C
main()

# 3. Name format
print("")

# Part A
def nameFormat(first, last, middle=None):
    if middle:                                                            # If middle name is provided
        return f"{last.title()}, {first.title()}, {middle[0].upper()}."   # Formats the name as "Last, First, with middle initial"
    else:                                                                 # If middle name is not provided
        return f"{last.title()}, {first.title()}"                         # Formats the name as "Last, First" without middle initial

# Part B
def main():
    print(nameFormat(first="james", last="bond"))                         # Calls the nameFormat function without a middle name and prints the result
    print(nameFormat(first="henry", last="jones", middle="indiana"))      # Calls the nameFormat function with a middle name and prints the result

# Part C
main()

print("")

# 4. Print Arbitrary Values
# Part A
def printNames(*names):
    print(" ".join(names))                                                # Joins and prints all arguments passed as names

# Part B
printNames("Ann", "Bianca", "Coco", "Dora", "Emily")

print("")

# 5. Dictionary
# Part A
def createUser(**kwargs):
    return kwargs                                                         # Returns a dictionary from keyword arguments

# Part B
def printUser(user):
    for key, value in user.items():                                       # Loops through the dictionary and prints each key-value pair
        print(f"{key}: {value}")                                          # Prints dictionary contents

# Part C
user1 = createUser(name="John", age=43, job="Programmer", hobby="Biking") # Creates a dictionary for user John with age, job, and hobby details
printUser(user1)                                                          # Prints the details of user John

print()

# Part D
user2 = createUser(name="Sara", age=24, school="QCC", major="CSIS")       # Creates a dictionary for user Sara with age, school, and major details
printUser(user2)                                                          # Prints the details of user Sara

print("")

# Computational Functions
# 6. Averaging
import random                                                             # Import the random module for generating random numbers

# Part A
def average(*grades):
    return sum(grades) / len(grades)                                      # Calculates and returns the average of the numbers provided as arguments

# Part B
def main():
    avg1 = average(95, 87, 83, 74)                                        # Calls the average function with predefined grades
    print(f"Average of 95, 87, 83, 74: {avg1:.2f}")                       # Prints the average of the given grades, rounded to 2 decimal places
    
    x = random.randint(-100, 0)                                           # Generate random integer in range -100 to 0
    y = random.randint(0, 100)                                            # Generate random integer in range 0 to 100
    avg2 = average(x, y)                                                  # Calls the average function with the random integers
    print(f"Average of any two random numbers, {x}, {y}: {avg2:.2f}")     # Prints the average of the random integers, rounded to 2 decimal places

# Part C
main()
