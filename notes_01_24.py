""" 
1. built-in types in python (https://docs.python.org/3/library/stdtypes.html)
2. ifs / for loops
3. talk about git (tutorial)
4. Live coding examples 
"""

# convert from a string to an integer 
x = "3"
x = int(x)
print(x)

# convert from a int to an float
y = 3 
y = float(y)
print(y)

# abs function 
z = -3.2
print(abs(z)) 

# convert to a string
id_ = 123456
print(str(id_))

# you can see what is loaded into your python program by running dir()
# print(dir())

# lists in python are mutable (can be changed)
lst  = [1,2,3]

# because the list is mutable we can update different entries in it
lst[0] = 4
print(lst)

#str_ -> avoid using built-in types/functions for your variable names

# strings in python are immutable (CANNOT be changed)
str_ = "This is a test"

# this will throw an error because strings are immutable
# -> TypeError: 'str' object does not support item assignment
# str_[0] = "A"

# to do this in python we need to always create a new variable
new_str = "A" + str_[1:]
print(new_str)


# SOME MORE PYTHON DATATYPES 

# SETS
# a set has no repeated elements and no order 
# useful for getting the unique elements when order does not matter
lst_  = [1,1,2,3,4,5]
print(set(lst_)) # -> 1,2,3,4,5 

# DICTIONARY
# dictionary : one of the most important data types in python 
# dictionary are a non-ordered data structure of key value pairs
stuff = dict() #defining a dictionary 
stuff = {} # alternate way to define a dictionary 
stuff["one"] = 1
stuff["two"] = 2
print(stuff)

# TUPLES ie.: time series data, coordinates 
# i.e. 1: (hr, min, sec)
# i.e. 2: (lat, long) 
# more memory efficient than a list
# tuples are immutable 
stuff2 = tuple() #define a tuple 
stuff2 = (1,2) # define a tuple
print(stuff2)
# stuff2[0] = 5 -> TypeError: 'tuple' object does not support item assignment

# you can also have tuples of many sizes 
stuff2 = (1,2,3,4)
print(stuff2[3])


# FOR LOOPS 

some_stuff = ["a","b","c"]

# simple for loop example
for x in some_stuff:
    print(x)

# loop with indicies using enumerate()
for idx, x in enumerate(some_stuff):
    print(idx, x)

#i.e. print out all the even numbered elements 
for idx, x in enumerate(some_stuff):

    # check if the index is even
    if idx % 2 == 0:
        print(x)

print("----------------------------")
#i.e. a more advanced example 
cars = ['Ford','Tesla','Mercedes']
for i,car in enumerate(cars):
    # f-strings: allow you to format text with live python code
    print(f'index = {i} and the element is {car} or {cars[i]}')

print("----------------------------")


def even_or_odd(n):
    """
    write a function that prints if each number is even or odd up to n 
    """
    # loop over given number n
    # range allows us to iterate over an integer
    for i in range(n):
        if i == 0:
            print(f"zero is neither even or odd")

        # check whether i is divisible by 2 
        elif i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd") 

print(even_or_odd(5))

"""

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""

def fizz_buzz(n):
    arr_ = []
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr_.append("FizzBuzz")
        elif i % 3 == 0:
            arr_.append("Fizz")
        elif i % 5 == 0:
            arr_.append("Buzz")
        else:
            arr_.append(f"{i}")
    return arr_

print(fizz_buzz(15))


# SOME OTHER COOL THINGS RANGE DOES 

# generate a list of numbers from 0 - 5
print(list(range(5)))

# generate a list of numbers , selecting only every second number
# between 1 and 5
print(list(range(1,5,2)))

# increment backwards with range 
for i in range(5,0,-1):
    print(f"Counting down.. {i}")

# write a program that takes a user input for a string
# and prints out every third letter of the string 

# 1. get input from user  
# 2. print put every third letter of the string 

# i.e. every_third("every third") -> e  i 

def every_third():
    s = input('--> ') # we can get input from the user.

    # start at index 2, (third letter) , step is going to be 3
    for i in range(2, len(s), 3):
        print(f"Letter {s[i]} at index {i}")

#every_third()

# deconstructing is another way to access each element of a tuple
# saving it to a variable
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)



