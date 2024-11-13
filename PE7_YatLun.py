# Question 1: Request an integer input, and then print whether the number is a multiple of 10 or not.
number = int(input("Enter an integer number, and I'll tell you if it's a multiple of ten: "))

if number % 10 == 0:                             # Check if the number is divisible by 10
    print(f"{number} is a multiple of ten.")     # If the condition is true, print the number is a multiple of ten
else:    
    print(f"{number} is not a multiple of ten.") # If the condition is false, print the number is not a multiple of ten

print("")

# Question 2: For & While
# Part A
for num in range(1, 1001):                       # Loop through numbers from 1 to 1000    
    if num % 2 == 0 and num % 3 == 0:            # Check if the number is even and a multiple of 3        
        print(num, end=" ")                      # Print the number if it meets the condition, end=" " keeps numbers on the same line
print()                                          # Print a newline

# Part B
num = 1                                          # Initialize variable to start at 1

while num <= 1000:                               # Loop until num exceeds 1000    
    if num % 2 == 0 and num % 3 == 0:            # Check if the number is even and a multiple of 3        
        print(num, end=" ")                      # Print the number if it meets the condition, end=" " keeps numbers on the same line    
    num += 1                                     # Increment num by 1 for the next iteration
print()                                          # Print a newline

print("")

# Question 3: Loop & Calculation
# Part A
total_sum = 0                                    # Initialize a variable to store the total sum

for num in range(1, 101):                        # Loop through numbers from 1 to 100    
    total_sum += num                             # Add each number to total_sum

print(f"Sum = {total_sum}")                      # Print the final total sum

# Part B
total_sum = 0                                    # Initialize total_sum to store the sum and num to start from the first even number which is 2
num = 2

while num <= 100:                                # Loop until num exceeds 100    
    total_sum += num                             # Add each number to total_sum    
    num += 2                                     # Move to the next even number by incrementing num by 2

print(f"Sum = {total_sum}")                      # Print the final total sum

print("")

# Question 4: Use a loop to print all the numbers are odd and multiples of 5 from 1 to n inclusive.
n = input("Enter a positive number: ")           # Request user input and store it in variable n

try:                                             # Use try-except to handle non-integer inputs    
    n = int(n)                                   # Convert input to an integer    
    if n > 0:                                    # Check if the input is a positive number    
        print(f"Range = 1 to {n}")               # If valid, print the range description        
        for num in range(1, n + 1):              # Loop through numbers from 1 to n
            
            if num % 2 != 0 and num % 5 == 0:    # Check if the number is odd and a multiple of 5
                print(num, end=" ")              # Print the number if it meets the condition, end=" " keeps numbers on the same line                
        print()                                  # Print a newline
    else:        
        print(f"Range = 1 to {n}")
        print("Invalid input.")                  # If the number is not positive, print an invalid input message
except ValueError:    
    print("Invalid input.")                      # If input is not a number, print an invalid input message

print("")

# Question 5: While & For
# Part A
num = 9                     # Initialize the starting number

while num >= 1:             # Use a while loop to count down from 9 to 1    
    print(num)              # Print the current number    
    num -= 1                # Decrement the number by 1

# Part B
print("Happy New Year!")    # Print the message after the countdown

# Part C
for num in range(9, 0, -1): # Use a for loop to count down from 9 to 1    
    print(num)              # Print the current number

# Part B
print("Happy New Year!")    # Print the message after the countdown

print("")

# Question 6: While & Lists
# Part A
import random                                                       # Import the random module to generate random grades
num_grades = int(input("Enter the number of grades in the list: ")) 

# Part B
grades = []                                                         # Initialize an empty list to store grades
for _ in range(num_grades):                                         # Loop num_grades times
    grade = random.randint(1, 100)                                  # Generate a random grade between 1 and 100
    grades.append(grade)                                            # Add the generated grade to the list

# Part C
passing_grade = int(input("Enter the passing grade: "))

# Part D
passGrades = [grade for grade in grades if grade >= passing_grade]  # Use list comprehension to filter passing grades

# Part E
print("Updated List:", passGrades)                                  # List of grades that passed
print("Original List:", grades)                                     # Original list of all generated grades

print("")

# Question 7: Sentinel While Loop
# Part A
numbers = []                                            # Initialize an empty list to store the numbers

while True:                                             # Use a while loop to continuously request numbers until the user enters 0    
    user_input = input("Enter a number or 0 to stop: ") # Request input from the user    
    number = float(user_input)                          # Convert the input to a float to handle both integers and decimal values
    
# Part C    
    if number == 0:                                     # Check if the entered number is 0
        break                                           # Exit the loop if the number is 0

# Part B    
    numbers.append(number)                              # Add the number to the list if it's not 0

# Part D
total_sum = sum(numbers)                                # Calculate the sum and average of the numbers in the list
average = total_sum / len(numbers) if numbers else 0    # Prevent division by 0

print(f"\nSum = {total_sum:.2f}")                       # Print the results in the specified format
print(f"Average = {average:.2f}")
print("Number(s) entered:")
print(" ".join(map(str, numbers)))                      # Join the list elements into a single line separated by spaces

print("")

# Question 8: Loop and Input
# Part A & B
n1 = int(input("Enter the first number (n1): "))        # Request first integer input from the user and store it in n1
n2 = int(input("Enter the second number (n2): "))       # Request second integer input from the user and store it in n2

# Part C 
if n1 < n2:                                             # If n1 is smaller than n2, execute the following block
    current = n1                                        # Initialize 'current' to start from n1
    while current <= n2:                                # Continue loop while current is less than or equal to n2
        print(current, end=" ")                         # Print current number with a space, stay on the same line
        current += 1                                    # Increment current by 1 to move to the next number
    print()                                             # Print a newline

# Part D
elif n1 > n2:                                           # If n1 is greater than n2, execute the following block
    for current in range(n1, n2 - 1, -1):               # Use a for loop to count down from n1 to n2
        print(current, end=" ")                         # Print current number with a space, stay on the same line
    print()                                             # Print a newline

# Part E
else:                                                   # If n1 is equal to n2
    print("n1 = n2")                                    # Print a message indicating that the two numbers are equal

print("")

# Question 9: Loop and Input
# Part A
lower = int(input("Enter the lower bound: "))           # Request the lower bound from the user
upper = int(input("Enter the upper bound: "))           # Request the upper bound from the user

# Part B
incVal = int(input("Enter the increment value: "))      # Request an increment value from the user

# Part C
print("USING WHILE LOOP")                               # Use a while loop to print values from lower to upper in increments of incVal
current = lower
while current <= upper:
    print(current, end=" ")                             # Print current value in the same line with a space
    current += incVal                                   # Increase current by the increment value
print()                                                 # Newline after loop ends

# Part D
print("\nUSING WHILE LOOP")                             # Use a while loop to vertically print all values in between each increment (each number on a new line)
current = lower
while current <= upper:
    print(current)                                      # Print current value on a new line
    current += incVal                                   # Increase current by the increment value

# Part E
print("\nUSING FOR LOOP")                               # Use a for loop to vertically print all values in between each increment
for current in range(lower, upper + 1, incVal):
    print(current)                                      # Print current value on a new line
