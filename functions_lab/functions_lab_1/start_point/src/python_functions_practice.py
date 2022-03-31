def return_10():
    return 10

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a,b):
    return int(a)+int(b)

def number_to_full_month_name(a):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[(a-1)]

def number_to_short_month_name(a):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[(a-1)]

def cubed_side_length(a):
    return a**3

def string_reversed(a):
    return a[::-1]

def conversionFC(f):
    return int((f-32)*(5/9))