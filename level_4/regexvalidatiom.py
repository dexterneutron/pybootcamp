""" Exercise 3 Create a decorator that makes sure that all 
function arguments where it's applied will match the regex on the regex exercise above.
"""
import functools,re

def match_regex(input_str):
    regex = '^[a-z]+_[a-z]+$'

    if(re.search(regex, input_str)):
        return True

    return False

def check_regex(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        arg_list = map(match_regex,args)
        kwargs_items = list(kwargs.values())
        kwargs_items = map(match_regex, kwargs_items)

        if all(arg_list) and all(kwargs_items):
            return func(*args, **kwargs)
        else:
            print("Wrong input!")
        # Do something after
    return wrapper_decorator

@check_regex
def print_input(*args, **kwargs):
    args = args if args else ""
    kwargs = kwargs if kwargs else ""
    print(args,kwargs)

#Test cases
#Positional arguments matching the regex
print_input("a_cb", "a_b", "a_c")
#Keyword arguments matching the regex 
print_input(name="a_b",name2="a_c") 
#Positional/Keyword arguments matching the regex
print_input("a_cb", "a_b", "a_c", name="a_b",name2="a_c") 
#Positional arguments not matching the regex
print_input("a__cb", "a_b", "a_c")
#Keyword arguments not matching the regex
print_input(name="a__b",name2="a_c")
#Positional/Keyword arguments not matching the regex
print_input("A_cb", "a_b", "a_c", name="a_b",name2="a_C")
#Positional arguments matching,Keyword arguments not matching the regex
print_input("a_cb", "a_b", "a_c", name="a_B",name2="a_c")
#Positional arguments not matching,Keyword arguments matching the regex
print_input("a__cb", "a_b", "a_c", name="a_b",name2="a_c")

