def addition(x,m):
    return x + m + 2
   

sum = addition(2,1) + 4
print(sum)

def func_name(name):
    return name
name = func_name("Ada")
print(f"Hello {name}")

def subtract(a,b):

    return a - b

result = subtract(7, subtract(4,2))

print(result)

# Excercise

def display_message():

    return "Hello everyone, I am learning about function definition and call"

print(display_message())


def favorite_book(title):
    var_1 = (f"One of my Favorite book is {title}")
    print(var_1)

favorite_book("Alice in a wonderland")