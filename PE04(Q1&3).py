#1)A – C, determine the output displayed by the lines of code.

#Part A 
print("Python")                              #This will result in Python being printed.
print("Python"[0])                           #This will display the first indice, which is P.
print("Python"[-1])                          #[-1] will give me the last element in my string, which is n. 
print("Python"[:])                           #[:] will print the entirety of the string. It doesn't specfic where the slice begins or end, so the output will be Python.  

#Part B
str = "Python 123"                            #The variable str is Python 123. 
print(str)                                    #The variable will be the output, which is Python 123. 
print(str[0])                                 #Position 0 of the string will be printed, which is P. 
print(str[-1])                                #The last element of the string will be printed, which is 3. 
print(str[:])                                 #The slice, does not specfic the position, so the entire string will be printed, which is Python 123. 

#Part C
strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"       #The variable strNum is created with a string of numbers. 
print(strNum[1], strNum[-1], len(strNum))     #[1] will be , and [-1] will be 9, len will give you the length of the variable which is 28.
print(strNum[:len(strNum)])                   #The beginning of the slice will be 0, and the ending will be the length of the variable. 
print(strNum[1]+strNum[-3])                   #The concatenation of [1], which is , and [-3], which is , will be ,,

#2)Use list methods to code below.

n = []                                        #a)Create an empty list called n.

n.append(2)                                   #b)Add 2 and 4 into the list.
n.append(4)

print(n)                                      #c)Print the list

n.insert(0,'0')                               #d)Add 0, 1 and 3 in proper order
n.insert(1,'1')
n.insert(3,'3')

print(n)                                      #e)Print the list

n.insert(5,'5')                               #f)Add 5 in proper order.

print(n)                                      #g)Print the list

del n[0]                                      #h)Remove 0 from the list.

print(n)                                      #i)Print the list.

removed_2 = n.pop(n.index(2))                 #j)Remove and print 2 from the list.
print(removed_2)

print(n)                                      #k)Print the list.

removed_4 = n.pop(n.index(4))                 #l)Remove and print 4 from the list.
print(removed_4)

print(n)                                      #m)Print the list.

sum_removed = removed_2 + removed_4           #n)Add all the removed numbers and print the sum.
print(sum_removed)                          

n[0] = 100                                    #o)Change the first item to 100 and last item to 9.9.
n[-1] = 9.9
                                
newNum = n.copy()                             #p) Copy the list n to a newNum list.

n.clear()                                     #q) Clear the list n.

print("Original list (newNum):", newNum)      #r) Print the original list, n and the newNum list
print("Cleared list (n):", n)       

del n                                         #s) Delete the list n.


#3)Write the codes and precisely produce the output format below.

Courses = ['MA 440', 'TECH 100','ET 574','ET 704']              #a)Create a list called courses containing the names of your current courses

print(Courses)                                                  #b)Print the list of courses.

print(f'I am taking{len(Courses)} courses.')                    #c)Use the len method to print “I am taking X courses” where X is the number of courses in the list.

print("First course:", Courses[0])                              #d)Using indexes to print the first and last item from the list.
print("Last course:", Courses[-1])

print("First four courses:", Courses[:4])                       #e)Using slicing to print the first four classes.

print("Last four courses:", Courses[-4:])                       #f)Using slicing to print the last four classes.

print("Courses except for the first and last:", Courses[1:-1])  #g)Using slicing to print the classes except for the first and last classes

