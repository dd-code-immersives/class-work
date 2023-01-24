""" 
2. Write a function that prints every second character of a given string 

i.e. second_char("AaBbCcDd") -> abcd
i.e. second_char("HeEeLlLlOo") -> hello

3. Write a function that reverses a given string using []

i.e. second_char("abcd") -> dcba
i.e. second_char("hello") -> olleh

"""

def second_char(str_):
    """
    returns every second character of a string
    """
    return str_[1::2]

def reverse(str_):
    """
    returns reverse of inputted string
    """
    # start= 0, end = length of string, step -1
    # hello 
    return str_[::-1]

# alternate one liner for a function
def reverse_alt(str_): return str_[::-1]

# "arrow" function in python aka lambda 
reverse_lambda = lambda x: x[::-1]

# reverse_alt and reverse_lambda are logically equivalent

# letters = "AaBbCcDd"
# #print(letters.index("B"))
# print(second_char("AaBbCcDd"))
# print(reverse("Hello"))
print(reverse_lambda("Hello"))