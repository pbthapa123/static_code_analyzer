import os, sys  

def calculate(a, b):
    if a > 0:
        if b > 0:
            return a * b
    else:
        if a == 0:
            return b
        else:
            return 0
    
    print("This will never print")  

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello " + self.name + " you are " + self.age + " years old.")  
        

def useless_function():
    pass  

user_input = input("Enter a number: ")
print("You entered:", user_input * 2)  

data = [1, 2, 3, 4, 5]
for i in range(len(data)):  
    print(data[i])  

x = 42
x = "Now I'm a string" 


print(undeclared_variable)

