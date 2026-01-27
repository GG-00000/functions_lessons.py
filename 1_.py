# function = A block of reusable code
#  place () after the function name to invoke it
# Methods, Help & Documentation Practice #1
def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} old")
    print("Happy birthday to you")
    print()

happy_birthday("Bro, 20")
happy_birthday("Steve, 21")
happy_birthday("joe, 23")

# Remove the characters to the left of our main text:
def display_invoice(username, amount, due_date):
   print(F"Hello {username}")
   print(F"Your bill of ${amount: .2f} is due: {due_date}")
   display_invoice("JoeSchmo", 100.10, "01/02")
   display_invoice("Gerardo", 1000000, "6/7")

def add(x,  y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x * y
    return z
def division(x, y):
    z = x / y 
    return z


print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(division(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongerbob", "squarepants")

print(full_name)

# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.

