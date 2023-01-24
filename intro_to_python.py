""" 
Basic Python operations

# for single line comments  ]

Some basic python operations
we use every day.
"""

#WORKING WITH NUMBERS

# addition
result = 3 + 3 
print(result)

# subtraction 
sub_result =  3 - 3 
print(sub_result)  

# multiplication
mul_result = 3 * 3 
print(mul_result)

# division with remainder 
div_result = 3 / 2
print(div_result) 

# division with no remainder
div_no_remainder = 3 // 2
print(div_no_remainder)

# power function 
power_result  =  2 ** 4
print(power_result)

# mod function 
mod_result = 3 % 2 
print(mod_result)

# WORKING WITH STRINGS 

name = "dom"
print(name)

# escape special characters with \
title = "dom\'s"
print(title)

#accessing characters in a string
# NOTE: Every string is a character array 
# this is why we can access by index using [] brackets
print(name[1])


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

word = "Python"
print(word[:2])
print(word[:3])

# [::] operator is very powerful for processing strings
# [start:end:step]  
# where start defaults to 0, end defaults to -1 , step defaults 1 
#  

# i.e. Reverse a string
# starting at index 0, ending at index -1 (end of string) step -1
print(word[::-1])

# i.e. get every second character for the string between
# the indicies of 0 and 5
print(word[0:5:2]) 
# or  
print(word[:5:2]) 



# WRITING A FUNCTION with a return value
def add_one(n):
    res = n + 1 
    return res
# WRITING A FUNCTION without a return value 
def print_value(n):
    print(n)

print(add_one(3))
print_value(3)







