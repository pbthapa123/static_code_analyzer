import os, sys  

def calculate(a, b):

    # Nested conditional logic to perform multiplication or return values 
    if a > 0:
        if b > 0:
            return a * b
    else:
        if a == 0:
            return b
        else:
            return 0
    
    print("This will never print")  # Unreachable code: this line will never be executed due to return statements above
 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age          # No type checking: if age is not a string, concatenation in greeting() may fail

    def greeting(self):
        print("Hello " + self.name + " you are " + self.age + " years old.")  
        

def useless_function():
    pass                     # Useless function: defined but never called or used

user_input = input("Enter a number: ")
print("You entered:", user_input * 2)  # Logic issue: input is a string, so '3' becomes '33', not the numeric result 6

data = [1, 2, 3, 4, 5]
for i in range(len(data)):  
    print(data[i])  # Less Pythonic: better to use 'for item in data:' for cleaner and more efficient iteration


x = 42
x = "Now I'm a string"   # Type reassignment: reassigning a variable to a different type can lead to confusion or bugs



