# Question 4

# a
grades = [] # Create an empty list

# b
grades.append(90) # Add grades
grades.append(55)
grades.append(82)
grades.append(33)
grades.append(70)

# c
print("Current List:", grades) # Output: Current List: [90, 55, 82, 33, 70]

# d
total = 0 # Compute total
for grade in grades:
    total += grade

# e
average = total / len(grades) # Compute average

# f
print(f"Average: {average:.2f}") # Output: Average: 66.00

# g
grades = [grade for grade in grades if grade >= 60] # Remove failing grades

# h
print("Updated list:", grades) # Output: Updated list: [90, 82, 70]

# i
updated_average = sum(grades) / len(grades) # Compute updated average
print(f"Updated Average: {updated_average:.3f}") # Output: Updated Average: 80.667

#Question 5

# a
full_name = input("Enter the full name of your favorite US president:\n") # Prompt for name

# b
first_name, last_name = full_name.split() # Split into first and last names
print(f"First Name: {first_name.capitalize()}") # Output first name
print(f"Last Name: {last_name.capitalize()}") # Output last name
