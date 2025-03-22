class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

def create_person(name, age):
    person = Person(name, age)
    return person

def main():
    p1 = create_person("Alice", "25")  # Error: age should be an integer, not a string
    p1.say_hello()

    p2 = create_person("Bob", 30)
    p2.say_hello()
    
    p3 = create_person("Charlie")  # Error: Missing the age parameter
    p3.say_hello()

if __name__ == "__main__":
    main()