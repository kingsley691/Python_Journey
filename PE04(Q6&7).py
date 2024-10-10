# Question 6 : A – H, determine and explain the output displayed by the lines of code.

# Part A
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n, n[:])      #The output from this code will be "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]". It shows the same list stored from the variable "n" twice with the brackets.   
print(n[0], n[-10]) #The output from this code will be "1 1". The code "n[0]" shows the first element from the list which is 1 and "n[-10]" will show the number in the -10th position which also happens to be one. Negative indices start from -1, which is always the last value of the list.
print(n[9], n[-1])  #The output from this code will be "10 10". The code "n[9]" shows the number in the 9th position, starting from 0 from the list which is 10 and "n[-1]" will show the last number of the list.
print(n[3:])        #The output from this code will be "[4, 5, 6, 7, 8, 9, 10]". The code "n[3:]" means that it will only show all the elements from indices 3 and beyond.  
print(n[:5])        #The output from this code will be "[1, 2, 3, 4, 5]". The code "n[:5]" means that it will only show all the elements before the indice 5 which is 6 on the list.  
print(n[-5:-1])     #The output from this code will be "[6, 7, 8, 9]". The code "n[-5:-1]" means that it will only show all the elements starting from index -5 to the indices before index -1 as slicing does not show the end index. 
print(n[4:8])       #The output from this code will be "[5, 6, 7, 8]". The code "n[4:8]" means that it will only show all the elements starting from index 4 to the indice before index 8 as slicing does not show the end index. 

# Part B
print(n[-1] + n[-2])                       #The output from this code will be "19". The code "n[-1] + n[-2]" will add both values of index -1 and -2 together, resulting in 10+9 which equals to 19.
print(n[9] - n[1])                         #The output from this code will be "8". The code "n[9] - n[1]" will subtract both values of index 9 and 1, resulting in 10-2 which equals to 8.
print(n[2] * n[5])                         #The output from this code will be "18". The code "n[2] * n[5]" will multiply both values of index 2 and 5, resulting in 3*6 which equals to 18.
print(n[8] / n[2])                         #The output from this code will be "19". The code "n[8] / n[2]" will divide both values of index 8 and 2, resulting in 9/3 which equals to 3.0.
print(len(n), n[:len(n)], sep = '\n')      #The output from this code will be "10\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]". The function len will show the amount of items in a list which is 10 in this case, which also is also why it shows the whole list in the code "n[:len(n)]" as len(n) means to show all the elements. The command "sep = '\n'" will tell the print to separate each item by the newline command.     
print(min(n), max(n), type(n), sep = '\t') #The output from this code will be "1\t10\t<class 'list'.". The min function shows the element of the least value, the max function shows the element of the greatest value, and the type fuction determines what class/data the object is. The command "sep = '\t'" will tell the print to separate each item by the tab command. 

# Part C
n[0], n[9] = "apple", 'cherry'
n.insert(3, "banana")
n.insert(-1, "kiwi")
print(n)                                                 #The output of this code will be "['apple', 2, 3, 'banana', 4, 5, 6, 7, 8, 9, 'kiwi', 'cherry']. The codeline "n[0], n[9] = "apple", 'cherry'" changes the elements of indices 0 and 9 to the new elements apple and "cherry". Codelines "n.insert(3, "banana")" and "n.insert(-1, "kiwi")" adds in the assigned elements to the location of the index written.
print(f"Do you like {n[0].upper()} or {n[-1].upper()}?") #The output of this code will be "Do you like APPLE or CHERRY?". The function ".upper" capitializes the entire word the function is assigned to, it is possible thanks to the f before the first quotation marks which allows {n[0].upper()} and {n[-1].upper()} to work properly.

# Part D
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(-11)
n.append("orange")
n[0], n[1] = n[-1], n[-2]
print(n+n) #The output of this code will be "['orange', -11, 3, 4, 5, 6, 7, 8, 9, 10, -11, 'orange', 'orange', -11, 3, 4, 5, 6, 7, 8, 9, 10, -11, 'orange']. The append function inserts objects at the end of list which is 'orange' and -11 in this case. The codeline "n[0], n[1] = n[-1], n[-2]" assigns the element of index -1 and -2 to index 0 and 1, overwriting the previous element. The codeline "n+n" basically prints two lists of n and combine them to make one big list.
print(n*2) #The output of this code will be "['orange', -11, 3, 4, 5, 6, 7, 8, 9, 10, -11, 'orange', 'orange', -11, 3, 4, 5, 6, 7, 8, 9, 10, -11, 'orange']. The append function inserts objects at the end of list which is 'orange' and -11 in this case. The codeline "n[0], n[1] = n[-1], n[-2]" assigns the element of index -1 and -2 to index 0 and 1, overwriting the previous element. The codeline "n*n" is similar to the previous print codeline, combining the amount of list calculated from the equation.

# Part E
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item1 = n.pop(0)
print(f"{item1} is removed.")              #The output of this code will be "1 is removed". The "pop" function removes the item at the specified position which in this case, 1 is getting removed. The popped value is assigned to a new variable "item1", the f before the quotation marks allows item1 to work in print. 
item2 = n.pop()
print(f"{item2} is removed.")              #The output of this code will be "10 is removed". The "pop" function removes the item at the specified position which in this case, 1o is getting removed. The popped value is assigned to a new variable "item2", the f before the quotation marks allows item1 to work in print.
print('n = ', n)                           #The output of this code will be "n =  [2, 3, 4, 5, 6, 7, 8, 9]". The current list has had the value 1 and 10 popped/removed through item1 and item2.
print(f'Removed items: {item1} & {item2}') #The output of this code will be "Removed items: 1 & 10". The f=string allows the print to recognize variables, item1 and item2.

# Part F
n.insert(6, 'pear')
del n[-1]
del n[0]
print(n)          #The output of this code will be "[2, 3, 4, 5, 6, 'pear', 7, 8, 9]". The codeline "n.insert(6, 'pear')" will place the element pear in index 6, between 6 and 7 on the list. The del function removes the item with states index, that being 1 and 10 on the list.
n.remove("pear")
n.remove(6)
print('n = ', n)  #The output of this code will be "n =  [2, 3, 4, 5, 7, 8, 9]". Similar to del the function "remove" removes the specified value, in this case is 6 and 'pear' on. the list. The remove function differs from del from that the remove function gets rid of the first occurrence of the specified value. 
n.clear()
print(f'n = {n}') #The output of this code will be "n = []". The "clear" function empties all elements/values of a list which is why only the brackets are left.

# Part G
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry']
fruits.sort()
print(fruits[0], fruits[-1]) #The output of this code will be "apple pear". The function "sort" will sort a list in alphabetical order. So the list would now look like "['apple', 'cherry', 'kiwi', 'orange', 'pear']". The element apple is at index 0 and pear is at index -1.
fruits.sort(reverse=True)
print(fruits[0], fruits[-1]) #The output of this code will be "pear apple". The codeline "fruits.sort(reverse=True)" will sort the list in alphabetical order and reverse the list. So the list would now look like "['pear', 'orange', 'kiwi', 'cherry', 'apple']". Now the element pear is at index 0 and apple is at index -1.

# Part H
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry']
print(sorted(fruits))               #The output of this code will be "['apple', 'cherry', 'kiwi', 'orange', 'pear']". Similar to the function "sort" it sorts the list in alphabetical order. The difference between sort and sorted is that the sort function is permanent and sorted gets a temporary copy of the list.
print(fruits[0], fruits[-1])        #The output of this code will be "kiwi cherry". Because the function sorted's effects are temporary, the list for this codeline is the original list of fruits. Which entails that kiwi is on index 1 and cherry is on index -1.
print(sorted(fruits, reverse=True)) #The output of this code will be "['pear', 'orange', 'kiwi', 'cherry', 'apple']". Similar to the function "sort(reverse=True)", it sorts the list in alphabetical order and reverses the order. And because the function used is sorted, the effects are temporary.
print(fruits[0], fruits[-1])        #The output of this code will be "kiwi cherry". It is the same case as the previous code before "print(fruits[0], fruits[-1])". The reverse and alphabetical sorting of the list does not carry over to this code, function effects are not permanent.

print("")

# Question 7 : A – C, identify the errors and rewrite the statements in the correct syntax.

# Part A error
# print(myList[3]) is incorrect, the list may have three things but the indices start at zero. So the only indices you can print in the positive side is 0, 1, and 2 
myList = ['apple','banana','cherry']
print(myList[2])

# Part A - Second method
print(myList[-1])

# Part B error
# print(myList[-1:-4]) is incorrect because that code would print an empty list. The start index has to be less than the stop/last index
myList = ['apple','banana','cherry']
print(myList[-4:])

# Part B - Second method
print(myList[0:3])

# Part C error
# print(myList[-1:-4])
word = 'sea'
word = 'p' + word[1:]
print(word)

# Part C - Second method
word = ['sea']
word[0] = 'pea'
print(word[0])

# Part D error
# n = [1, "two", 'three', 4] is set up wrong, you cannot join together integer and strings 
n = ['1', "two", 'three', '4']
print(" ".join(n))

# Part D - Second method
n = [1, "two", 'three', 4]
del n[0]
del n[2]
n.insert(0,"1")
n.insert(3,"4")
print(" ".join(n))