# 1. Determine the output displayed by the lines of code. Save your code as PE8_1.py.
# NY gives the populations of the five boroughs in millions.
NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}
# Part A
print(NY['QS'])                                          # Output: 2.25
print(NY.get("QS"))                                      # Output: 2.25

print("")

# Part B
print(NY.get("LI", "Not in"))                            # Output: Not in
print(NY.get('SI', 'absent'))                            # Output: 0.47
print(NY.setdefault('SI', 0.48))                         # Output: 0.47

print("")

# Part C
print("LI" in NY)                                        # Output: False
print('MN' not in NY)                                    # Output: False

print("")

# Part D
print(len(NY), min(NY), max(NY))                         # Output: 5 BN SI
print(len(NY.items()), max(NY.keys()), min(NY.values())) # Output: 5 SI 0.47

print("")

# Part E
print(round(NY['QS']))                                   # Output: 2
NY['QS'] += 0.3
print(round(NY['QS'], 1))                                # Output: 2.5

print("")

# Part F
print(NY.keys())                                         # Output: dict_keys(['BX', 'MN', 'QS', 'BN', 'SI'])
print(list(NY.values()))                                 # Output: [1.42, 1.63, 2.55, 2.56, 0.47]
print(tuple(NY.items()))                                 # Output: (('BX', 1.42), ('MN', 1.63), ('QS', 2.55), ('BN', 2.56), ('SI', 0.47))

print("")

# Part G
total = 0
for x in NY.values():
    total += x
print(f'{total:.1f}')                                    # Output: 8.6

print("")

# Part H
total = 0
for x in NY:
    total += NY[x]
print(f'{total:.1f}')                                    # Output: 8.6

print("")

# Part I
for x in sorted(NY):
    print(x, end='|')                                    # Output: BN|BX|MN|QS|SI|

print("")

# Part J
for x in sorted(NY, reverse=True):                       # Sort keys in reverse alphabetical order
    print(x, end='|')                                    # Output: SI|QS|MN|BX|BN|

print("")

# Part K
for value in sorted(NY.values(), reverse=True):          # Sort values in descending order
    print(value, end=', ')                               # Output: 2.56, 2.55, 1.63, 1.42, 0.47,

print("")

# Part L
if "QS" in NY:
    print("Queens is the most diverse county in NY.")    # Output: Queens is the most diverse county in NY.

print("")

# Part M
for x, y in NY.items():
    if x == 'BN' and y > 2.5:                            # Check if the key is 'BN' and its value is greater than 2.5
        print(f"{x} is the Kings county!")               # Output: BN is the Kings county!

print("")

# Part N
NY["SK"] = 1.49
print(NY)                                                # Output: {'BX': 1.42, 'MN': 1.63, 'QS': 2.55, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49}

print("")

# Part O
NY.update({"NU":1.34})
print(NY)                                                # Output: {'BX': 1.42, 'MN': 1.63, 'QS': 2.55, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}

print("")

# Part P
NY.pop("QS")
NY.popitem()
print(NY)                                                # Output: {'BX': 1.42, 'MN': 1.63, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49}

print("")

# Part Q
newYork = NY
del newYork['BN']
print(NY)                                                # Output: {'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49}
print(newYork)                                           # Output: {'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49}

print("")

# Part R
newYork = dict(NY)
del newYork["BX"]                                        # Change to BX because BN was deleted already
print(len(NY))                                           # Output: 4
print(len(newYork))                                      # Output: 3

print("")

# Part S
NewYork = NY.copy()
NY.clear()
print(NY)                                                # Output: {}
print(NewYork)                                           # Output: {'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49}
del NY
print(set(NewYork))                                      # Output: {'SK', 'MN', 'SI', 'BX'}

print("")

# 2. Convert the following two lists into one dictionary:
keys = ['Ten', 'Twenty', 'Thirty']               # List of string keys
values = [10, 20, 30]                            # List of integer values
result = dict(zip(keys, values))                 # Pair keys and values, then convert to dictionary
print(result)                                    # Print resulting dictionary

print("")

# 3. Merge the following two dictionaries into one dictionary:
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}  # First dictionary
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50} # Second dictionary
merged_dict = {**dict1, **dict2}                 # Merge dictionaries with unpacking
print(merged_dict)                               # Print merged dictionary

print("")

# 4. Create a dictionary and use loops to print keys and values:
# Part A
stuInfo = {"name": "Kingsley", "gpa": 3.8, "age": 20} # Define student info dictionary
print(stuInfo)
print()

# Part B
for key, value in stuInfo.items():                    # Loop through the dictionary's keys and values using items()
    print(f"{key}: {value}", end=" | ")
print()

# Part C
stuInfo.update({"gpa": 4.0})                          # Update the value of 'gpa' to 4.0 using the update() method
print(stuInfo)
print()

# Part D
for key in stuInfo.keys():                            # Loop through the dictionary's keys and values using keys()
    print(f"{key}: {stuInfo[key]}", end=" | ")
print()

# Part E
stuInfo["major"] = "CSIS"                             # Add a new key 'major' with the value 'CSIS'
print(stuInfo)
print()

# Part F
for value in stuInfo.values():                        # Loop through the dictionary's values
    print(value, end=" | ")
print()

# Part G
stuInfo.pop("gpa")                                    # Remove the key 'gpa' from the dictionary
stuInfo.pop("age")                                    # Remove the key 'age' from the dictionary

# Part H
print(stuInfo)                                        # Print the final version of the updated dictionary

print("")

# 5. Displays a rank in the defined dictionary.
# Part A
rank = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"} # Define rank levels

# Part B
year = (int(input("Enter number of years: ")))                   # Request user input for years

# Part C and D
print(rank.get(year, "Invalid input"))                           # Print rank or error message

print("")

# 6. Nest dictionaries within a list, stuClass.
# Part A
stu1 = {'name': 'Dilon', 'gpa': 3.5}
stu2 = {'name': 'Grace', 'gpa': 3.8}
stu3 = {'name': 'AJ', 'gpa': 3.2}

# Part B
stuClass = [stu1, stu2, stu3]                                     # List containing all student dictionaries
print(stuClass)                                                   # Print the list of student dictionaries

# Part C
for student in stuClass:
    print(student)                                                # Print each student dictionary

# Part D
for student in stuClass:                                          # Access and print the GPA of each student
    print(student['gpa'], end=" | ")
print()                                         

# Part E
stuClass[-1]['gpa'] = 4.0                                         # Set the GPA of the last student to 4.0

# Part F
stuClass.append({'name': 'Jane', 'gpa': 3.6})                     # Add a new student to the list

# Part G
for student in stuClass:
    print(f"{student['name']:<15} {student['gpa']:.1f}")          # Print name and GPA

print("")

# 7a. Implement the following:
# Part A
letters = [chr(i) for i in range(97, 123)]        # Use chr to convert ASCII to characters

# Part B
numbers = list(range(1, 27))                      # Range from 1 to 26 inclusive

# Part C
charNum = dict(zip(letters, numbers))             # Zip letters and numbers into key-value pairs

# Part D
for key, value in charNum.items():
    print(f"{key}: {value}", end="|")             # Print each key-value pair

print("")

# 7b. Implement the following:
# Part A
letters_upper = [chr(i) for i in range(65, 91)]   # ASCII for uppercase letters

# Part B
numbers_large = list(range(100, 2700, 100))       # Step of 100 up to 2600

# Part C
numChar = dict(zip(letters_upper, numbers_large)) # Zip letters and numbers

# Part D
for key, value in numChar.items():
    print(f"{key}: {value}", end="|")             # Print key-value pairs

# Part E
all = {**charNum, **numChar}                      # Combine both dictionaries

# Part F
print(all)                                        # Print all key-value pairs in the merged dictionary
