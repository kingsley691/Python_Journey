# Question 1: A - O, determine the output displayed by the lines of code where a, b, c = 2, 3, 0.
a, b, c = 2, 3, 0

# Part A
print(a ** b == b ** a)                                           # Output: False (2^3 is 8, and 3^2 is 9; they are not equal)

# Part B
print(a < b or b < a)                                             # Output: True (2 is less than 3)

# Part C
print('dog' > 'cat' + 'mouse')                                    # Output: True, since 'd' comes after 'c' alphabetically, 'dog' is greater than 'catmouse'

# Part D
print('Car' < 'Train')                                            # Output: True, the ASCII value of 'C' (67) is less than the ASCII value of 'T' (84)

# Part E
print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b)))  # Output: False

# Part F
print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b)))   # Output: True

# Part G
print(not ((a < b) and (a < (b + a))))                            # Output: False

# Part H
print("small" > "large" and (not c))                              # Output: True

# Part I
print(isinstance(c, int))                                         # Output: True

# Part J
print(isinstance(3.14, float))                                    # Output: True

# Part K
if (a < b < c):
    b = c + a
else:
    b = c * a
print(b)                                                          # Output: 0 (c is 0, so c * a = 0)

# Part L
if ('A' in 'apple'):
    print("A as apple.")
else:
    print('Oops, not there.')                                     # Output: Oops, not there.

# Part M
x = 6
if (x < 0):
    print('negative')
else:
    if (x == 0):
        print('zero')
    else:
        print('positive')                                         # Output: positive

# Part N
n = 1
if n <= 9:
    print("Less than ten.")                                       # Output: Less than ten.
elif n == 1:
    print("Equal to one.")              

# Part O
let = input("Enter A, B or C: \n")
let = let.upper()
if (let == 'A'):
    print('\nA, my name is Alice.')
elif (let == 'B'):
    print('\nTo be, or not to be.')
elif (let == 'C'):
    print('\nOh, say, can you see.')
else:
    print('\nInvalid letter.')


print("")


# Question 2: Write an if-elif-else chain that determines a person’s stage of life.
age = 20                        # Example age

print(f"Age = {age}")           # Display age

if age < 0:
    print("Invalid age.")       # Output for negative ages
elif age < 2:
    print("You're a baby.")     # Output if the person is a baby
elif age < 4:
    print("You're a toddler.")  # Output if the person is a toddler
elif age < 13:
    print("You're a kid.")      # Output if the person is a kid
elif age < 20:
    print("You're a teenager.") # Output if the person is a teenager
elif age < 65:
    print("You're an adult.")   # Output if the person is a adult
else:
    print("You're an elder.")   # Output if the person is a elder


print("")


# Question 3: Implement the following to print a greeting to each user after they log in to a website
# Part A
usernames = ['Tom', 'Jerry', 'Bob', 'Dora', 'admin']                      # Create a list of usernames and admin

# Part E
if not usernames:                                                         # Check if the usernames list is empty
    print("We need to find some users.")                                  # Print this message if the list is empty
else:

# Part B                                                                  
    for user in usernames:                                                # Start a loop to iterate through each user in the list
                                                        
# Part C                                                
        if user.lower() == 'admin':                                       # Check if the current user is admin, using .lower() for case-insensitive
            print(f"Hello Admin, would you like to see a status report?") # Print a special message if the user is admin
            
# Part D
        else:
            print(f"Hello {user}, thank you for logging in again!")       # Print a greeting for any user who is not admin


print("")


# Question 4: Implement the following to simulate how websites ensure that everyone has a unique username.
# Part A
current_users = ['admin', 'tom', 'jerry', 'dora', 'GEORGE']    # Create the list of current users

# Part B
new_user = input("Enter your username: ")                      # Request the user to enter their username

# Part E
current_users_lower = [user.lower() for user in current_users] # Make sure the comparison is case-insensitive by converting both lists to lowercase

if new_user.lower() in current_users_lower:                    # Check if the new username (in lowercase) is already in the list

# Part C
    print(f"Sorry {new_user}, that name is taken.")            # If username is taken, print the message and display the current user list
    print("Current users:", current_users)
else:

# Part D
    print(f"Great, {new_user} is still available.")            # If username is available, add it to the current user list and print the updated list
    current_users.append(new_user)                             # Add the new username to the list
    print("Updated users:", current_users)                     # Print the updated users list


print("")


# Question 5: Implement the following to search a letter in a list.
# Part A
vehicles = ['car', 'Truck', 'boat', 'PLANE']     # Create the list of vehicles
print("Vehicles =", vehicles)                    # Display the list of vehicles

# Part B
search_letter = input("Enter a search letter: ") # Request the user to enter search letter

# Part C
if len(search_letter) != 1:                      # Check if the input is valid

# Part E
    print("Invalid search letter.")              # Print a message if more than one letter is entered
else:

# Part D
    for index, vehicle in enumerate(vehicles):                                            # Loop through each vehicle in the list and search for the letter
        if search_letter.lower() in vehicle.lower():                                      # Convert both the search letter and vehicle name to lowercase for case-insensitive comparison
            print(f"{vehicle} contains '{search_letter}' and it is in position {index}.") # Print the vehicle name and it's position if the letter is found
        else:
            print(f"{vehicle} does not contain '{search_letter}'.")                       # Print a message if the letter is not found in the vehicle name


print("")


# Question 6: A – D, identify the errors and rewrite the statement in the correct syntax.
# Part A
n = eval(input("Enter a number: "))
if n == 7:                                                              # Change '=' to '=='
    print("The square is", n * 2)

# Part B
n = 6
if 5 < n < 9:                                                           # Use chained comparison                    
    print("Yes")
else:
    print("No")

# Part C
major = "Computer Science"
if major == "Engineering Technology" or major == "Computer Technology": # Or should be lowercase(or), missing 'major ==' & closing parenthesis should be replaced with colon
    print("Yes")

# Part D
a, b = 1, 1.0
if a == b:                                                              # Change from '=' to '=='
    print("same")
